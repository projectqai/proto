import { createClient, type Client, ConnectError, Code } from "@connectrpc/connect";
import { createTransport } from "@connectrpc/connect/protocol-connect";
import type { UniversalClientFn } from "@connectrpc/connect/protocol";
import { create, clone } from "@bufbuild/protobuf";
import {
	WorldService,
	EntitySchema,
	EntityFilterSchema,
	ListEntitiesRequestSchema,
	EntityChangeRequestSchema,
	ConfigurableComponentSchema,
	ConfigurableState,
	EntityChange,
	LifetimeSchema,
	DeviceComponentSchema,
	DeviceState,
	ControllerSchema,
	InteractivityComponentSchema,
	type Entity,
} from "./dist/world_pb.js";
import { TimestampSchema } from "@bufbuild/protobuf/wkt";
import {
	MetricComponentSchema,
	MetricSchema,
	MetricKind,
	MetricUnit,
} from "./dist/metrics_pb.js";

export type WorldClient = Client<typeof WorldService>;

export { create } from "@bufbuild/protobuf";
export {
	EntitySchema,
	EntityFilterSchema,
	ListEntitiesRequestSchema,
	EntityChangeRequestSchema,
	EntityChange,
	type Entity,
} from "./dist/world_pb.js";

// fetch-based universal HTTP client for the Connect protocol.
// Works in Node, Bun, browsers, and goja — no http2 dependency.
const universalFetch: UniversalClientFn = async (req) => {
	const body = req.body ? await collectBytes(req.body) : undefined;
	// Prevent the server from gzip-encoding responses — the Connect
	// transport handles its own compression negotiation.
	req.header.set("Accept-Encoding", "identity");
	const resp = await fetch(req.url, {
		method: req.method,
		headers: req.header,
		body,
		signal: (req as any).signal,
	});
	return {
		status: resp.status,
		header: resp.headers,
		body: responseBodyStream(resp),
		trailer: new Headers(),
	};
};

async function collectBytes(iter: AsyncIterable<Uint8Array>): Promise<Uint8Array> {
	const chunks: Uint8Array[] = [];
	for await (const value of iter) {
		chunks.push(value);
	}
	const len = chunks.reduce((n, c) => n + c.length, 0);
	const out = new Uint8Array(len);
	let off = 0;
	for (const c of chunks) { out.set(c, off); off += c.length; }
	return out;
}

function responseBodyStream(resp: Response): AsyncIterable<Uint8Array> {
	if (!resp.body) return { [Symbol.asyncIterator]() { return { next: () => Promise.resolve({ done: true as const, value: undefined }), throw: () => Promise.resolve({ done: true as const, value: undefined }) }; } };
	const reader = resp.body.getReader();
	return {
		[Symbol.asyncIterator]() {
			return {
				async next() {
					const { done, value } = await reader.read();
					if (done) { reader.releaseLock(); return { done: true as const, value: undefined }; }
					return { done: false as const, value };
				},
				async throw(e: unknown) {
					reader.releaseLock();
					return { done: true as const, value: undefined };
				},
			};
		}
	};
}

export function connect(serverURL?: string): WorldClient {
	const base = serverURL ?? process.env.HYDRIS_SERVER ?? "http://localhost:50051";
	const transport = createTransport({
		baseUrl: base,
		httpClient: universalFetch,
		useBinaryFormat: true,
		interceptors: [],
		acceptCompression: [],
		sendCompression: null,
		compressMinBytes: Number.MAX_SAFE_INTEGER,
		readMaxBytes: Number.MAX_SAFE_INTEGER,
		writeMaxBytes: Number.MAX_SAFE_INTEGER,
	});
	return createClient(WorldService, transport);
}

export function push(client: WorldClient, ...entities: Entity[]) {
	return client.push(create(EntityChangeRequestSchema, { changes: entities }));
}

// Schema → typed config inference

type SchemaProperty = { readonly type: string; readonly default?: unknown; readonly [key: string]: unknown };
type SchemaProperties = Readonly<Record<string, SchemaProperty>>;

type InferProperty<P extends SchemaProperty> =
	P extends { type: "string" } ? string :
	P extends { type: "boolean" } ? boolean :
	P extends { type: "number" | "integer" } ? number :
	unknown;

export type InferConfig<S extends SchemaProperties> = {
	[K in keyof S]?: InferProperty<S[K]>;
};

function extractConfig<S extends SchemaProperties>(entity: Entity, schema: S): InferConfig<S> {
	const raw = entity.config?.value ?? {};
	const result: Record<string, unknown> = {};
	for (const [key, prop] of Object.entries(schema)) {
		const val = raw[key];
		result[key] = (val !== undefined && val !== null && typeof val === prop.type) ? val : prop.default;
	}
	return result as InferConfig<S>;
}

// Attach options

export type HealthResult = boolean | Record<number, { label: string; value: number | bigint }>;

export interface AttachOptions<S extends SchemaProperties> {
	id: string;
	label?: string;
	controller?: string;
	device?: { category?: string };
	icon?: string;
	schema: S;
	run: (client: WorldClient, config: InferConfig<S>, signal: AbortSignal) => Promise<void>;
	health?: () => HealthResult | Promise<HealthResult>;
	interval?: number;
	signal?: AbortSignal;
}

// Internals

const DEFAULT_INTERVAL = 10_000;

function isCanceled(err: unknown): boolean {
	return err instanceof ConnectError && err.code === Code.Canceled;
}

function sleep(ms: number, signal: AbortSignal): Promise<void> {
	return new Promise((resolve) => {
		if (signal.aborted) return resolve();
		const timer = setTimeout(resolve, ms);
		signal.addEventListener("abort", () => { clearTimeout(timer); resolve(); }, { once: true });
	});
}

/**
 * Attach to a single device entity. Registers the entity, starts a heartbeat
 * with TTL, watches for config changes, and runs the provided function.
 *
 * The health callback is polled every `interval` ms. Return `true` for healthy,
 * `false` to skip the heartbeat (device expires via TTL), or a metrics map
 * to push metrics alongside the heartbeat.
 */
export async function attach<S extends SchemaProperties>(opts: AttachOptions<S>) {
	const client = connect();
	const entityID = opts.id;
	const interval = opts.interval ?? DEFAULT_INTERVAL;
	const health = opts.health ?? (() => true);

	const entity = create(EntitySchema, {
		id: entityID,
		...(opts.label && { label: opts.label }),
		...(opts.controller && { controller: create(ControllerSchema, { id: opts.controller }) }),
		...(opts.device && { device: create(DeviceComponentSchema, opts.device) }),
		...(opts.icon && { interactivity: create(InteractivityComponentSchema, { icon: opts.icon }) }),
		configurable: create(ConfigurableComponentSchema, {
			schema: { type: "object", properties: opts.schema as Record<string, unknown> },
		}),
	});

	// Register entity without device — device is managed by heartbeat
	await push(client, create(EntitySchema, { ...entity, device: undefined }));
	console.log(`attached entity=${entityID}`);

	// Heartbeat

	let heartbeatId: ReturnType<typeof setInterval> | null = null;

	const pushHeartbeat = (result?: Record<number, { label: string; value: number | bigint }>) => {
		const e = create(EntitySchema, {
			id: entityID,
			device: create(DeviceComponentSchema, { ...entity.device, state: DeviceState.DeviceStateActive }),
			lifetime: create(LifetimeSchema, {
				until: create(TimestampSchema, { seconds: BigInt(Math.floor((Date.now() + interval + 1_000) / 1000)) }),
			}),
		});
		if (result) {
			e.metric = create(MetricComponentSchema, {
				metrics: Object.entries(result).map(([idStr, { label, value }]) =>
					typeof value === "bigint"
						? create(MetricSchema, { id: Number(idStr), label, kind: MetricKind.MetricKindCount, unit: MetricUnit.MetricUnitCount, val: { case: "uint64", value } })
						: create(MetricSchema, { id: Number(idStr), label, kind: MetricKind.MetricKindGauge, unit: MetricUnit.MetricUnitNone, val: { case: "float", value } }),
				),
			});
		}
		return push(client, e);
	};

	const outerAbort = new AbortController();
	const tick = async () => {
		if (outerAbort.signal.aborted) return;
		try {
			const r = await health();
			if (r !== false) await pushHeartbeat(r === true ? undefined : r);
		} catch { /* health check failed */ }
	};
	tick();
	heartbeatId = setInterval(tick, interval);

	// Config state management

	const pushState = async (entity: Entity, state: ConfigurableState, error?: string) => {
		const cfg = entity.configurable
			? clone(ConfigurableComponentSchema, entity.configurable)
			: create(ConfigurableComponentSchema);
		cfg.state = state;
		cfg.error = error;
		if (entity.config && state === ConfigurableState.ConfigurableStateActive) {
			cfg.appliedVersion = entity.config.version;
		}
		await push(client, create(EntitySchema, { id: entityID, configurable: cfg })).catch(() => { });
	};

	let runningAbort: AbortController | null = null;
	let currentConfigVersion = 0n;
	let currentEntity: Entity | null = null;

	const stop = () => {
		if (runningAbort) {
			const e = currentEntity;
			runningAbort.abort();
			runningAbort = null;
			currentEntity = null;
			console.log(`stopped entity=${entityID}`);
			if (e) pushState(e, ConfigurableState.ConfigurableStateInactive);
		}
	};

	const start = (e: Entity) => {
		runningAbort = new AbortController();
		currentEntity = e;
		const childSignal = runningAbort.signal;

		(async () => {
			while (!childSignal.aborted) {
				await pushState(e, ConfigurableState.ConfigurableStateStarting);
				await pushState(e, ConfigurableState.ConfigurableStateActive);

				try {
					await opts.run(client, extractConfig(e, opts.schema), childSignal);
				} catch (err) {
					if (childSignal.aborted || isCanceled(err)) return;
					console.error(`error, restarting entity=${entityID}`, err);
					await pushState(e, ConfigurableState.ConfigurableStateFailed, String(err));
				}

				await sleep(5_000, childSignal);
			}
		})();
	};

	// Watch for config changes

	const stream = client.watchEntities(
		create(ListEntitiesRequestSchema, { filter: create(EntityFilterSchema, { id: entityID }) }),
		...(opts.signal ? [{ signal: opts.signal }] : []),
	);

	try {
		for await (const event of stream) {
			if (!event.entity) continue;

			if (event.t === EntityChange.EntityChangeExpired || event.t === EntityChange.EntityChangeUnobserved) {
				stop();
				continue;
			}
			if (event.t !== EntityChange.EntityChangeUpdated) continue;

			const e = event.entity;
			if (!e.config) { stop(); continue; }
			if (e.config.version === currentConfigVersion && runningAbort) continue;

			stop();
			currentConfigVersion = e.config.version;
			start(e);
		}
	} catch (err) {
		if (!isCanceled(err)) throw err;
	} finally {
		stop();
		outerAbort.abort();
		if (heartbeatId) clearInterval(heartbeatId);
	}
}
