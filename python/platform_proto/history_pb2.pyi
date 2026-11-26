import components_pb2 as _components_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
import world_pb2 as _world_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HistoryTimeline(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HistoryTimelineUnspecified: _ClassVar[HistoryTimeline]
    HistoryTimelineFresh: _ClassVar[HistoryTimeline]
    HistoryTimelineAccepted: _ClassVar[HistoryTimeline]

class HistoryEventKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HistoryEventKindInvalid: _ClassVar[HistoryEventKind]
    HistoryEventKindTrackNew: _ClassVar[HistoryEventKind]
    HistoryEventKindTrackLost: _ClassVar[HistoryEventKind]
    HistoryEventKindAlert: _ClassVar[HistoryEventKind]
    HistoryEventKindSensor: _ClassVar[HistoryEventKind]
    HistoryEventKindLate: _ClassVar[HistoryEventKind]
HistoryTimelineUnspecified: HistoryTimeline
HistoryTimelineFresh: HistoryTimeline
HistoryTimelineAccepted: HistoryTimeline
HistoryEventKindInvalid: HistoryEventKind
HistoryEventKindTrackNew: HistoryEventKind
HistoryEventKindTrackLost: HistoryEventKind
HistoryEventKindAlert: HistoryEventKind
HistoryEventKindSensor: HistoryEventKind
HistoryEventKindLate: HistoryEventKind

class HistoryRangeRequest(_message.Message):
    __slots__ = ("timeline",)
    TIMELINE_FIELD_NUMBER: _ClassVar[int]
    timeline: HistoryTimeline
    def __init__(self, timeline: _Optional[_Union[HistoryTimeline, str]] = ...) -> None: ...

class HistoryRangeResponse(_message.Message):
    __slots__ = ("min", "max")
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    min: _timestamp_pb2.Timestamp
    max: _timestamp_pb2.Timestamp
    def __init__(self, min: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., max: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class HistoryLanesRequest(_message.Message):
    __slots__ = ("until", "filter", "timeline", "limit")
    FROM_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    TIMELINE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    until: _timestamp_pb2.Timestamp
    filter: _world_pb2.EntityFilter
    timeline: HistoryTimeline
    limit: int
    def __init__(self, until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., filter: _Optional[_Union[_world_pb2.EntityFilter, _Mapping]] = ..., timeline: _Optional[_Union[HistoryTimeline, str]] = ..., limit: _Optional[int] = ..., **kwargs) -> None: ...

class HistoryInterval(_message.Message):
    __slots__ = ("until",)
    FROM_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    until: _timestamp_pb2.Timestamp
    def __init__(self, until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., **kwargs) -> None: ...

class HistoryLane(_message.Message):
    __slots__ = ("entity_id", "label", "alive", "current", "identity")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    ALIVE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    entity_id: str
    label: str
    alive: _containers.RepeatedCompositeFieldContainer[HistoryInterval]
    current: _containers.RepeatedCompositeFieldContainer[HistoryInterval]
    identity: _world_pb2.ClassificationIdentity
    def __init__(self, entity_id: _Optional[str] = ..., label: _Optional[str] = ..., alive: _Optional[_Iterable[_Union[HistoryInterval, _Mapping]]] = ..., current: _Optional[_Iterable[_Union[HistoryInterval, _Mapping]]] = ..., identity: _Optional[_Union[_world_pb2.ClassificationIdentity, str]] = ...) -> None: ...

class HistoryLanesResponse(_message.Message):
    __slots__ = ("lanes", "capped")
    LANES_FIELD_NUMBER: _ClassVar[int]
    CAPPED_FIELD_NUMBER: _ClassVar[int]
    lanes: _containers.RepeatedCompositeFieldContainer[HistoryLane]
    capped: bool
    def __init__(self, lanes: _Optional[_Iterable[_Union[HistoryLane, _Mapping]]] = ..., capped: bool = ...) -> None: ...

class HistoryHistogramRequest(_message.Message):
    __slots__ = ("until", "bucket_ms", "timeline")
    FROM_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    BUCKET_MS_FIELD_NUMBER: _ClassVar[int]
    TIMELINE_FIELD_NUMBER: _ClassVar[int]
    until: _timestamp_pb2.Timestamp
    bucket_ms: int
    timeline: HistoryTimeline
    def __init__(self, until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., bucket_ms: _Optional[int] = ..., timeline: _Optional[_Union[HistoryTimeline, str]] = ..., **kwargs) -> None: ...

class HistoryEvent(_message.Message):
    __slots__ = ("at", "kind", "entity_id", "label", "identity")
    AT_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    at: _timestamp_pb2.Timestamp
    kind: HistoryEventKind
    entity_id: str
    label: str
    identity: _world_pb2.ClassificationIdentity
    def __init__(self, at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., kind: _Optional[_Union[HistoryEventKind, str]] = ..., entity_id: _Optional[str] = ..., label: _Optional[str] = ..., identity: _Optional[_Union[_world_pb2.ClassificationIdentity, str]] = ...) -> None: ...

class HistoryBucket(_message.Message):
    __slots__ = ("changes", "detections", "late", "affiliation")
    FROM_FIELD_NUMBER: _ClassVar[int]
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    DETECTIONS_FIELD_NUMBER: _ClassVar[int]
    LATE_FIELD_NUMBER: _ClassVar[int]
    AFFILIATION_FIELD_NUMBER: _ClassVar[int]
    changes: int
    detections: int
    late: int
    affiliation: HistoryAffiliationCounts
    def __init__(self, changes: _Optional[int] = ..., detections: _Optional[int] = ..., late: _Optional[int] = ..., affiliation: _Optional[_Union[HistoryAffiliationCounts, _Mapping]] = ..., **kwargs) -> None: ...

class HistoryAffiliationCounts(_message.Message):
    __slots__ = ("pending", "unknown", "friend", "neutral", "hostile", "suspect")
    PENDING_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_FIELD_NUMBER: _ClassVar[int]
    FRIEND_FIELD_NUMBER: _ClassVar[int]
    NEUTRAL_FIELD_NUMBER: _ClassVar[int]
    HOSTILE_FIELD_NUMBER: _ClassVar[int]
    SUSPECT_FIELD_NUMBER: _ClassVar[int]
    pending: int
    unknown: int
    friend: int
    neutral: int
    hostile: int
    suspect: int
    def __init__(self, pending: _Optional[int] = ..., unknown: _Optional[int] = ..., friend: _Optional[int] = ..., neutral: _Optional[int] = ..., hostile: _Optional[int] = ..., suspect: _Optional[int] = ...) -> None: ...

class HistoryHistogramResponse(_message.Message):
    __slots__ = ("bucket_ms", "buckets", "events")
    BUCKET_MS_FIELD_NUMBER: _ClassVar[int]
    BUCKETS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    bucket_ms: int
    buckets: _containers.RepeatedCompositeFieldContainer[HistoryBucket]
    events: _containers.RepeatedCompositeFieldContainer[HistoryEvent]
    def __init__(self, bucket_ms: _Optional[int] = ..., buckets: _Optional[_Iterable[_Union[HistoryBucket, _Mapping]]] = ..., events: _Optional[_Iterable[_Union[HistoryEvent, _Mapping]]] = ...) -> None: ...

class HistoryReadStreamRequest(_message.Message):
    __slots__ = ("entity_id", "component", "until", "keyframe", "timeline")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    KEYFRAME_FIELD_NUMBER: _ClassVar[int]
    TIMELINE_FIELD_NUMBER: _ClassVar[int]
    entity_id: str
    component: _components_pb2.EntityComponent
    until: _timestamp_pb2.Timestamp
    keyframe: bool
    timeline: HistoryTimeline
    def __init__(self, entity_id: _Optional[str] = ..., component: _Optional[_Union[_components_pb2.EntityComponent, str]] = ..., until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., keyframe: bool = ..., timeline: _Optional[_Union[HistoryTimeline, str]] = ..., **kwargs) -> None: ...

class RecordedSample(_message.Message):
    __slots__ = ("event", "citing")
    EVENT_FIELD_NUMBER: _ClassVar[int]
    CITING_FIELD_NUMBER: _ClassVar[int]
    event: _world_pb2.EntityChangeEvent
    citing: _containers.RepeatedCompositeFieldContainer[_world_pb2.Entity]
    def __init__(self, event: _Optional[_Union[_world_pb2.EntityChangeEvent, _Mapping]] = ..., citing: _Optional[_Iterable[_Union[_world_pb2.Entity, _Mapping]]] = ...) -> None: ...

class HistoryReadStreamResponse(_message.Message):
    __slots__ = ("samples",)
    SAMPLES_FIELD_NUMBER: _ClassVar[int]
    samples: _containers.RepeatedCompositeFieldContainer[RecordedSample]
    def __init__(self, samples: _Optional[_Iterable[_Union[RecordedSample, _Mapping]]] = ...) -> None: ...

class HistoryReplayRequest(_message.Message):
    __slots__ = ("at", "filter", "timeline", "speed", "limit")
    AT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    TIMELINE_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    at: _timestamp_pb2.Timestamp
    filter: _world_pb2.EntityFilter
    timeline: HistoryTimeline
    speed: float
    limit: int
    def __init__(self, at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., filter: _Optional[_Union[_world_pb2.EntityFilter, _Mapping]] = ..., timeline: _Optional[_Union[HistoryTimeline, str]] = ..., speed: _Optional[float] = ..., limit: _Optional[int] = ...) -> None: ...

class HistoryReplayResponse(_message.Message):
    __slots__ = ("at", "entities", "changes", "live", "capped")
    AT_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    LIVE_FIELD_NUMBER: _ClassVar[int]
    CAPPED_FIELD_NUMBER: _ClassVar[int]
    at: _timestamp_pb2.Timestamp
    entities: _containers.RepeatedCompositeFieldContainer[_world_pb2.Entity]
    changes: _containers.RepeatedCompositeFieldContainer[_world_pb2.EntityChangeEvent]
    live: bool
    capped: bool
    def __init__(self, at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., entities: _Optional[_Iterable[_Union[_world_pb2.Entity, _Mapping]]] = ..., changes: _Optional[_Iterable[_Union[_world_pb2.EntityChangeEvent, _Mapping]]] = ..., live: bool = ..., capped: bool = ...) -> None: ...

class HistoryClearRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HistoryClearResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HistoryIndexEntry(_message.Message):
    __slots__ = ("time", "chunk")
    TIME_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    chunk: int
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., chunk: _Optional[int] = ...) -> None: ...

class HistoryIndex(_message.Message):
    __slots__ = ("keyframes", "citations", "buckets", "events", "routing_channels", "internal", "foreign", "views", "chunks")
    class Keyframes(_message.Message):
        __slots__ = ("channel", "entries")
        CHANNEL_FIELD_NUMBER: _ClassVar[int]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        channel: int
        entries: _containers.RepeatedCompositeFieldContainer[HistoryIndexEntry]
        def __init__(self, channel: _Optional[int] = ..., entries: _Optional[_Iterable[_Union[HistoryIndexEntry, _Mapping]]] = ...) -> None: ...
    class Citations(_message.Message):
        __slots__ = ("entity_id", "entries")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        entity_id: str
        entries: _containers.RepeatedCompositeFieldContainer[HistoryIndexEntry]
        def __init__(self, entity_id: _Optional[str] = ..., entries: _Optional[_Iterable[_Union[HistoryIndexEntry, _Mapping]]] = ...) -> None: ...
    class View(_message.Message):
        __slots__ = ("accepted", "chunk", "keyframe_time")
        ACCEPTED_FIELD_NUMBER: _ClassVar[int]
        CHUNK_FIELD_NUMBER: _ClassVar[int]
        KEYFRAME_TIME_FIELD_NUMBER: _ClassVar[int]
        accepted: _timestamp_pb2.Timestamp
        chunk: int
        keyframe_time: _timestamp_pb2.Timestamp
        def __init__(self, accepted: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., chunk: _Optional[int] = ..., keyframe_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class Chunk(_message.Message):
        __slots__ = ("offset", "length", "start", "end", "first_accepted", "channels")
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        START_FIELD_NUMBER: _ClassVar[int]
        END_FIELD_NUMBER: _ClassVar[int]
        FIRST_ACCEPTED_FIELD_NUMBER: _ClassVar[int]
        CHANNELS_FIELD_NUMBER: _ClassVar[int]
        offset: int
        length: int
        start: _timestamp_pb2.Timestamp
        end: _timestamp_pb2.Timestamp
        first_accepted: _timestamp_pb2.Timestamp
        channels: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ..., start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., first_accepted: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., channels: _Optional[_Iterable[int]] = ...) -> None: ...
    KEYFRAMES_FIELD_NUMBER: _ClassVar[int]
    CITATIONS_FIELD_NUMBER: _ClassVar[int]
    BUCKETS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    ROUTING_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_FIELD_NUMBER: _ClassVar[int]
    FOREIGN_FIELD_NUMBER: _ClassVar[int]
    VIEWS_FIELD_NUMBER: _ClassVar[int]
    CHUNKS_FIELD_NUMBER: _ClassVar[int]
    keyframes: _containers.RepeatedCompositeFieldContainer[HistoryIndex.Keyframes]
    citations: _containers.RepeatedCompositeFieldContainer[HistoryIndex.Citations]
    buckets: _containers.RepeatedCompositeFieldContainer[HistoryBucket]
    events: _containers.RepeatedCompositeFieldContainer[HistoryEvent]
    routing_channels: _containers.RepeatedScalarFieldContainer[str]
    internal: bool
    foreign: bool
    views: _containers.RepeatedCompositeFieldContainer[HistoryIndex.View]
    chunks: _containers.RepeatedCompositeFieldContainer[HistoryIndex.Chunk]
    def __init__(self, keyframes: _Optional[_Iterable[_Union[HistoryIndex.Keyframes, _Mapping]]] = ..., citations: _Optional[_Iterable[_Union[HistoryIndex.Citations, _Mapping]]] = ..., buckets: _Optional[_Iterable[_Union[HistoryBucket, _Mapping]]] = ..., events: _Optional[_Iterable[_Union[HistoryEvent, _Mapping]]] = ..., routing_channels: _Optional[_Iterable[str]] = ..., internal: bool = ..., foreign: bool = ..., views: _Optional[_Iterable[_Union[HistoryIndex.View, _Mapping]]] = ..., chunks: _Optional[_Iterable[_Union[HistoryIndex.Chunk, _Mapping]]] = ...) -> None: ...
