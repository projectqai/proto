import geometry_pb2 as _geometry_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
import metrics_pb2 as _metrics_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Priority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PriorityUnspecified: _ClassVar[Priority]
    PriorityRoutine: _ClassVar[Priority]
    PriorityImmediate: _ClassVar[Priority]
    PriorityFlash: _ClassVar[Priority]

class CameraProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CameraProtocolUnspecified: _ClassVar[CameraProtocol]
    CameraProtocolWebrtc: _ClassVar[CameraProtocol]
    CameraProtocolHls: _ClassVar[CameraProtocol]
    CameraProtocolMjpeg: _ClassVar[CameraProtocol]
    CameraProtocolImage: _ClassVar[CameraProtocol]
    CameraProtocolIframe: _ClassVar[CameraProtocol]

class ClassificationIdentity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ClassificationIdentityInvalid: _ClassVar[ClassificationIdentity]
    ClassificationIdentityPending: _ClassVar[ClassificationIdentity]
    ClassificationIdentityUnknown: _ClassVar[ClassificationIdentity]
    ClassificationIdentityFriend: _ClassVar[ClassificationIdentity]
    ClassificationIdentityNeutral: _ClassVar[ClassificationIdentity]
    ClassificationIdentityHostile: _ClassVar[ClassificationIdentity]
    ClassificationIdentitySuspect: _ClassVar[ClassificationIdentity]

class ClassificationBattleDimension(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ClassificationBattleDimensionInvalid: _ClassVar[ClassificationBattleDimension]
    ClassificationBattleDimensionUnknown: _ClassVar[ClassificationBattleDimension]
    ClassificationBattleDimensionSpace: _ClassVar[ClassificationBattleDimension]
    ClassificationBattleDimensionAir: _ClassVar[ClassificationBattleDimension]
    ClassificationBattleDimensionGround: _ClassVar[ClassificationBattleDimension]
    ClassificationBattleDimensionSeaSurface: _ClassVar[ClassificationBattleDimension]
    ClassificationBattleDimensionSubsurface: _ClassVar[ClassificationBattleDimension]

class NavigationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NavigationModeUnspecified: _ClassVar[NavigationMode]
    NavigationModePlanned: _ClassVar[NavigationMode]
    NavigationModeStationary: _ClassVar[NavigationMode]
    NavigationModeUnderway: _ClassVar[NavigationMode]
    NavigationModeAutonomous: _ClassVar[NavigationMode]
    NavigationModeGuided: _ClassVar[NavigationMode]
    NavigationModeLoitering: _ClassVar[NavigationMode]
    NavigationModeReturning: _ClassVar[NavigationMode]

class LinkStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LinkStatusUnspecified: _ClassVar[LinkStatus]
    LinkStatusConnected: _ClassVar[LinkStatus]
    LinkStatusDegraded: _ClassVar[LinkStatus]
    LinkStatusLost: _ClassVar[LinkStatus]

class DeviceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DeviceStatePending: _ClassVar[DeviceState]
    DeviceStateActive: _ClassVar[DeviceState]
    DeviceStateFailed: _ClassVar[DeviceState]

class ConfigurableState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ConfigurableStateInactive: _ClassVar[ConfigurableState]
    ConfigurableStateStarting: _ClassVar[ConfigurableState]
    ConfigurableStateActive: _ClassVar[ConfigurableState]
    ConfigurableStateFailed: _ClassVar[ConfigurableState]
    ConfigurableStateConflict: _ClassVar[ConfigurableState]
    ConfigurableStateScheduled: _ClassVar[ConfigurableState]

class EntityChange(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EntityChangeInvalid: _ClassVar[EntityChange]
    EntityChangeUpdated: _ClassVar[EntityChange]
    EntityChangeExpired: _ClassVar[EntityChange]
    EntityChangeUnobserved: _ClassVar[EntityChange]

class TaskStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TaskStatusInvalid: _ClassVar[TaskStatus]
    TaskStatusRunning: _ClassVar[TaskStatus]
    TaskStatusCompleted: _ClassVar[TaskStatus]
    TaskStatusFailed: _ClassVar[TaskStatus]
PriorityUnspecified: Priority
PriorityRoutine: Priority
PriorityImmediate: Priority
PriorityFlash: Priority
CameraProtocolUnspecified: CameraProtocol
CameraProtocolWebrtc: CameraProtocol
CameraProtocolHls: CameraProtocol
CameraProtocolMjpeg: CameraProtocol
CameraProtocolImage: CameraProtocol
CameraProtocolIframe: CameraProtocol
ClassificationIdentityInvalid: ClassificationIdentity
ClassificationIdentityPending: ClassificationIdentity
ClassificationIdentityUnknown: ClassificationIdentity
ClassificationIdentityFriend: ClassificationIdentity
ClassificationIdentityNeutral: ClassificationIdentity
ClassificationIdentityHostile: ClassificationIdentity
ClassificationIdentitySuspect: ClassificationIdentity
ClassificationBattleDimensionInvalid: ClassificationBattleDimension
ClassificationBattleDimensionUnknown: ClassificationBattleDimension
ClassificationBattleDimensionSpace: ClassificationBattleDimension
ClassificationBattleDimensionAir: ClassificationBattleDimension
ClassificationBattleDimensionGround: ClassificationBattleDimension
ClassificationBattleDimensionSeaSurface: ClassificationBattleDimension
ClassificationBattleDimensionSubsurface: ClassificationBattleDimension
NavigationModeUnspecified: NavigationMode
NavigationModePlanned: NavigationMode
NavigationModeStationary: NavigationMode
NavigationModeUnderway: NavigationMode
NavigationModeAutonomous: NavigationMode
NavigationModeGuided: NavigationMode
NavigationModeLoitering: NavigationMode
NavigationModeReturning: NavigationMode
LinkStatusUnspecified: LinkStatus
LinkStatusConnected: LinkStatus
LinkStatusDegraded: LinkStatus
LinkStatusLost: LinkStatus
DeviceStatePending: DeviceState
DeviceStateActive: DeviceState
DeviceStateFailed: DeviceState
ConfigurableStateInactive: ConfigurableState
ConfigurableStateStarting: ConfigurableState
ConfigurableStateActive: ConfigurableState
ConfigurableStateFailed: ConfigurableState
ConfigurableStateConflict: ConfigurableState
ConfigurableStateScheduled: ConfigurableState
EntityChangeInvalid: EntityChange
EntityChangeUpdated: EntityChange
EntityChangeExpired: EntityChange
EntityChangeUnobserved: EntityChange
TaskStatusInvalid: TaskStatus
TaskStatusRunning: TaskStatus
TaskStatusCompleted: TaskStatus
TaskStatusFailed: TaskStatus

class Entity(_message.Message):
    __slots__ = ("id", "label", "controller", "lifetime", "priority", "lease", "geo", "symbol", "camera", "detection", "bearing", "track", "locator", "kinematics", "shape", "classification", "transponder", "administrative", "orientation", "navigation", "power", "capture", "taskable", "device", "config", "configurable", "mission", "link", "metric", "sensor", "local_shape", "interactivity")
    ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    LIFETIME_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    LEASE_FIELD_NUMBER: _ClassVar[int]
    GEO_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    CAMERA_FIELD_NUMBER: _ClassVar[int]
    DETECTION_FIELD_NUMBER: _ClassVar[int]
    BEARING_FIELD_NUMBER: _ClassVar[int]
    TRACK_FIELD_NUMBER: _ClassVar[int]
    LOCATOR_FIELD_NUMBER: _ClassVar[int]
    KINEMATICS_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    TRANSPONDER_FIELD_NUMBER: _ClassVar[int]
    ADMINISTRATIVE_FIELD_NUMBER: _ClassVar[int]
    ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    NAVIGATION_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_FIELD_NUMBER: _ClassVar[int]
    TASKABLE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONFIGURABLE_FIELD_NUMBER: _ClassVar[int]
    MISSION_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    SENSOR_FIELD_NUMBER: _ClassVar[int]
    LOCAL_SHAPE_FIELD_NUMBER: _ClassVar[int]
    INTERACTIVITY_FIELD_NUMBER: _ClassVar[int]
    id: str
    label: str
    controller: Controller
    lifetime: Lifetime
    priority: Priority
    lease: Lease
    geo: GeoSpatialComponent
    symbol: SymbolComponent
    camera: CameraComponent
    detection: DetectionComponent
    bearing: BearingComponent
    track: TrackComponent
    locator: LocatorComponent
    kinematics: KinematicsComponent
    shape: GeoShapeComponent
    classification: ClassificationComponent
    transponder: TransponderComponent
    administrative: AdministrativeComponent
    orientation: OrientationComponent
    navigation: NavigationComponent
    power: PowerComponent
    capture: CaptureComponent
    taskable: TaskableComponent
    device: DeviceComponent
    config: ConfigurationComponent
    configurable: ConfigurableComponent
    mission: MissionComponent
    link: LinkComponent
    metric: _metrics_pb2.MetricComponent
    sensor: SensorComponent
    local_shape: LocalShapeComponent
    interactivity: InteractivityComponent
    def __init__(self, id: _Optional[str] = ..., label: _Optional[str] = ..., controller: _Optional[_Union[Controller, _Mapping]] = ..., lifetime: _Optional[_Union[Lifetime, _Mapping]] = ..., priority: _Optional[_Union[Priority, str]] = ..., lease: _Optional[_Union[Lease, _Mapping]] = ..., geo: _Optional[_Union[GeoSpatialComponent, _Mapping]] = ..., symbol: _Optional[_Union[SymbolComponent, _Mapping]] = ..., camera: _Optional[_Union[CameraComponent, _Mapping]] = ..., detection: _Optional[_Union[DetectionComponent, _Mapping]] = ..., bearing: _Optional[_Union[BearingComponent, _Mapping]] = ..., track: _Optional[_Union[TrackComponent, _Mapping]] = ..., locator: _Optional[_Union[LocatorComponent, _Mapping]] = ..., kinematics: _Optional[_Union[KinematicsComponent, _Mapping]] = ..., shape: _Optional[_Union[GeoShapeComponent, _Mapping]] = ..., classification: _Optional[_Union[ClassificationComponent, _Mapping]] = ..., transponder: _Optional[_Union[TransponderComponent, _Mapping]] = ..., administrative: _Optional[_Union[AdministrativeComponent, _Mapping]] = ..., orientation: _Optional[_Union[OrientationComponent, _Mapping]] = ..., navigation: _Optional[_Union[NavigationComponent, _Mapping]] = ..., power: _Optional[_Union[PowerComponent, _Mapping]] = ..., capture: _Optional[_Union[CaptureComponent, _Mapping]] = ..., taskable: _Optional[_Union[TaskableComponent, _Mapping]] = ..., device: _Optional[_Union[DeviceComponent, _Mapping]] = ..., config: _Optional[_Union[ConfigurationComponent, _Mapping]] = ..., configurable: _Optional[_Union[ConfigurableComponent, _Mapping]] = ..., mission: _Optional[_Union[MissionComponent, _Mapping]] = ..., link: _Optional[_Union[LinkComponent, _Mapping]] = ..., metric: _Optional[_Union[_metrics_pb2.MetricComponent, _Mapping]] = ..., sensor: _Optional[_Union[SensorComponent, _Mapping]] = ..., local_shape: _Optional[_Union[LocalShapeComponent, _Mapping]] = ..., interactivity: _Optional[_Union[InteractivityComponent, _Mapping]] = ...) -> None: ...

class Controller(_message.Message):
    __slots__ = ("id", "node")
    ID_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    id: str
    node: str
    def __init__(self, id: _Optional[str] = ..., node: _Optional[str] = ...) -> None: ...

class Lease(_message.Message):
    __slots__ = ("controller", "expires")
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_FIELD_NUMBER: _ClassVar[int]
    controller: str
    expires: _timestamp_pb2.Timestamp
    def __init__(self, controller: _Optional[str] = ..., expires: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Lifetime(_message.Message):
    __slots__ = ("until", "fresh")
    FROM_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    FRESH_FIELD_NUMBER: _ClassVar[int]
    until: _timestamp_pb2.Timestamp
    fresh: _timestamp_pb2.Timestamp
    def __init__(self, until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., fresh: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., **kwargs) -> None: ...

class GeoSpatialComponent(_message.Message):
    __slots__ = ("longitude", "latitude", "altitude", "covariance")
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    COVARIANCE_FIELD_NUMBER: _ClassVar[int]
    longitude: float
    latitude: float
    altitude: float
    covariance: CovarianceMatrix
    def __init__(self, longitude: _Optional[float] = ..., latitude: _Optional[float] = ..., altitude: _Optional[float] = ..., covariance: _Optional[_Union[CovarianceMatrix, _Mapping]] = ...) -> None: ...

class SymbolComponent(_message.Message):
    __slots__ = ("milStd2525C",)
    MILSTD2525C_FIELD_NUMBER: _ClassVar[int]
    milStd2525C: str
    def __init__(self, milStd2525C: _Optional[str] = ...) -> None: ...

class InteractivityComponent(_message.Message):
    __slots__ = ("icon", "reference_url")
    ICON_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_URL_FIELD_NUMBER: _ClassVar[int]
    icon: str
    reference_url: str
    def __init__(self, icon: _Optional[str] = ..., reference_url: _Optional[str] = ...) -> None: ...

class Camera(_message.Message):
    __slots__ = ("label", "url", "protocol", "fov", "range_min", "range_max")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    FOV_FIELD_NUMBER: _ClassVar[int]
    RANGE_MIN_FIELD_NUMBER: _ClassVar[int]
    RANGE_MAX_FIELD_NUMBER: _ClassVar[int]
    label: str
    url: str
    protocol: CameraProtocol
    fov: float
    range_min: float
    range_max: float
    def __init__(self, label: _Optional[str] = ..., url: _Optional[str] = ..., protocol: _Optional[_Union[CameraProtocol, str]] = ..., fov: _Optional[float] = ..., range_min: _Optional[float] = ..., range_max: _Optional[float] = ...) -> None: ...

class CameraComponent(_message.Message):
    __slots__ = ("cameras",)
    CAMERAS_FIELD_NUMBER: _ClassVar[int]
    cameras: _containers.RepeatedCompositeFieldContainer[Camera]
    def __init__(self, cameras: _Optional[_Iterable[_Union[Camera, _Mapping]]] = ...) -> None: ...

class DetectionComponent(_message.Message):
    __slots__ = ("detectorEntityId", "classification", "lastMeasured")
    DETECTORENTITYID_FIELD_NUMBER: _ClassVar[int]
    CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    LASTMEASURED_FIELD_NUMBER: _ClassVar[int]
    detectorEntityId: str
    classification: str
    lastMeasured: _timestamp_pb2.Timestamp
    def __init__(self, detectorEntityId: _Optional[str] = ..., classification: _Optional[str] = ..., lastMeasured: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class BearingComponent(_message.Message):
    __slots__ = ("azimuth", "elevation")
    AZIMUTH_FIELD_NUMBER: _ClassVar[int]
    ELEVATION_FIELD_NUMBER: _ClassVar[int]
    azimuth: float
    elevation: float
    def __init__(self, azimuth: _Optional[float] = ..., elevation: _Optional[float] = ...) -> None: ...

class SensorComponent(_message.Message):
    __slots__ = ("coverage",)
    COVERAGE_FIELD_NUMBER: _ClassVar[int]
    coverage: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, coverage: _Optional[_Iterable[str]] = ...) -> None: ...

class Quaternion(_message.Message):
    __slots__ = ("x", "y", "z", "w")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    w: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ..., w: _Optional[float] = ...) -> None: ...

class CovarianceMatrix(_message.Message):
    __slots__ = ("mxx", "mxy", "mxz", "myy", "myz", "mzz")
    MXX_FIELD_NUMBER: _ClassVar[int]
    MXY_FIELD_NUMBER: _ClassVar[int]
    MXZ_FIELD_NUMBER: _ClassVar[int]
    MYY_FIELD_NUMBER: _ClassVar[int]
    MYZ_FIELD_NUMBER: _ClassVar[int]
    MZZ_FIELD_NUMBER: _ClassVar[int]
    mxx: float
    mxy: float
    mxz: float
    myy: float
    myz: float
    mzz: float
    def __init__(self, mxx: _Optional[float] = ..., mxy: _Optional[float] = ..., mxz: _Optional[float] = ..., myy: _Optional[float] = ..., myz: _Optional[float] = ..., mzz: _Optional[float] = ...) -> None: ...

class OrientationComponent(_message.Message):
    __slots__ = ("orientation", "covariance", "roll_rate", "pitch_rate", "yaw_rate")
    ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    COVARIANCE_FIELD_NUMBER: _ClassVar[int]
    ROLL_RATE_FIELD_NUMBER: _ClassVar[int]
    PITCH_RATE_FIELD_NUMBER: _ClassVar[int]
    YAW_RATE_FIELD_NUMBER: _ClassVar[int]
    orientation: Quaternion
    covariance: CovarianceMatrix
    roll_rate: float
    pitch_rate: float
    yaw_rate: float
    def __init__(self, orientation: _Optional[_Union[Quaternion, _Mapping]] = ..., covariance: _Optional[_Union[CovarianceMatrix, _Mapping]] = ..., roll_rate: _Optional[float] = ..., pitch_rate: _Optional[float] = ..., yaw_rate: _Optional[float] = ...) -> None: ...

class TrackComponent(_message.Message):
    __slots__ = ("tracker", "history", "prediction")
    TRACKER_FIELD_NUMBER: _ClassVar[int]
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    tracker: str
    history: str
    prediction: str
    def __init__(self, tracker: _Optional[str] = ..., history: _Optional[str] = ..., prediction: _Optional[str] = ...) -> None: ...

class LocatorComponent(_message.Message):
    __slots__ = ("locatedEntityId",)
    LOCATEDENTITYID_FIELD_NUMBER: _ClassVar[int]
    locatedEntityId: str
    def __init__(self, locatedEntityId: _Optional[str] = ...) -> None: ...

class TaskableContext(_message.Message):
    __slots__ = ("entityId",)
    ENTITYID_FIELD_NUMBER: _ClassVar[int]
    entityId: str
    def __init__(self, entityId: _Optional[str] = ...) -> None: ...

class TaskableAssignee(_message.Message):
    __slots__ = ("entityId",)
    ENTITYID_FIELD_NUMBER: _ClassVar[int]
    entityId: str
    def __init__(self, entityId: _Optional[str] = ...) -> None: ...

class TaskableComponent(_message.Message):
    __slots__ = ("reserved", "label", "context", "assignee", "schema")
    RESERVED_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    reserved: str
    label: str
    context: _containers.RepeatedCompositeFieldContainer[TaskableContext]
    assignee: _containers.RepeatedCompositeFieldContainer[TaskableAssignee]
    schema: _struct_pb2.Struct
    def __init__(self, reserved: _Optional[str] = ..., label: _Optional[str] = ..., context: _Optional[_Iterable[_Union[TaskableContext, _Mapping]]] = ..., assignee: _Optional[_Iterable[_Union[TaskableAssignee, _Mapping]]] = ..., schema: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class KinematicsEnu(_message.Message):
    __slots__ = ("east", "north", "up", "covariance")
    EAST_FIELD_NUMBER: _ClassVar[int]
    NORTH_FIELD_NUMBER: _ClassVar[int]
    UP_FIELD_NUMBER: _ClassVar[int]
    COVARIANCE_FIELD_NUMBER: _ClassVar[int]
    east: float
    north: float
    up: float
    covariance: CovarianceMatrix
    def __init__(self, east: _Optional[float] = ..., north: _Optional[float] = ..., up: _Optional[float] = ..., covariance: _Optional[_Union[CovarianceMatrix, _Mapping]] = ...) -> None: ...

class KinematicsComponent(_message.Message):
    __slots__ = ("velocityEnu", "accelerationEnu")
    VELOCITYENU_FIELD_NUMBER: _ClassVar[int]
    ACCELERATIONENU_FIELD_NUMBER: _ClassVar[int]
    velocityEnu: KinematicsEnu
    accelerationEnu: KinematicsEnu
    def __init__(self, velocityEnu: _Optional[_Union[KinematicsEnu, _Mapping]] = ..., accelerationEnu: _Optional[_Union[KinematicsEnu, _Mapping]] = ...) -> None: ...

class Geometry(_message.Message):
    __slots__ = ("wkb", "planar")
    WKB_FIELD_NUMBER: _ClassVar[int]
    PLANAR_FIELD_NUMBER: _ClassVar[int]
    wkb: bytes
    planar: _geometry_pb2.PlanarGeometry
    def __init__(self, wkb: _Optional[bytes] = ..., planar: _Optional[_Union[_geometry_pb2.PlanarGeometry, _Mapping]] = ...) -> None: ...

class GeoShapeComponent(_message.Message):
    __slots__ = ("geometry",)
    GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    geometry: Geometry
    def __init__(self, geometry: _Optional[_Union[Geometry, _Mapping]] = ...) -> None: ...

class LocalShapeComponent(_message.Message):
    __slots__ = ("relative_to", "geometry")
    RELATIVE_TO_FIELD_NUMBER: _ClassVar[int]
    GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    relative_to: str
    geometry: _geometry_pb2.LocalGeometry
    def __init__(self, relative_to: _Optional[str] = ..., geometry: _Optional[_Union[_geometry_pb2.LocalGeometry, _Mapping]] = ...) -> None: ...

class ClassificationComponent(_message.Message):
    __slots__ = ("dimension", "identity")
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    dimension: ClassificationBattleDimension
    identity: ClassificationIdentity
    def __init__(self, dimension: _Optional[_Union[ClassificationBattleDimension, str]] = ..., identity: _Optional[_Union[ClassificationIdentity, str]] = ...) -> None: ...

class TransponderAIS(_message.Message):
    __slots__ = ("mmsi", "imo", "callsign", "vessel_name")
    MMSI_FIELD_NUMBER: _ClassVar[int]
    IMO_FIELD_NUMBER: _ClassVar[int]
    CALLSIGN_FIELD_NUMBER: _ClassVar[int]
    VESSEL_NAME_FIELD_NUMBER: _ClassVar[int]
    mmsi: int
    imo: int
    callsign: str
    vessel_name: str
    def __init__(self, mmsi: _Optional[int] = ..., imo: _Optional[int] = ..., callsign: _Optional[str] = ..., vessel_name: _Optional[str] = ...) -> None: ...

class TransponderADSB(_message.Message):
    __slots__ = ("icao_address", "flight_id")
    ICAO_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    FLIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    icao_address: int
    flight_id: str
    def __init__(self, icao_address: _Optional[int] = ..., flight_id: _Optional[str] = ...) -> None: ...

class TransponderComponent(_message.Message):
    __slots__ = ("ais", "adsb")
    AIS_FIELD_NUMBER: _ClassVar[int]
    ADSB_FIELD_NUMBER: _ClassVar[int]
    ais: TransponderAIS
    adsb: TransponderADSB
    def __init__(self, ais: _Optional[_Union[TransponderAIS, _Mapping]] = ..., adsb: _Optional[_Union[TransponderADSB, _Mapping]] = ...) -> None: ...

class AdministrativeComponent(_message.Message):
    __slots__ = ("id", "flag", "owner", "manufacturer", "model", "year_built", "length_m", "tonnage_gt", "engine_power_kw")
    ID_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    YEAR_BUILT_FIELD_NUMBER: _ClassVar[int]
    LENGTH_M_FIELD_NUMBER: _ClassVar[int]
    TONNAGE_GT_FIELD_NUMBER: _ClassVar[int]
    ENGINE_POWER_KW_FIELD_NUMBER: _ClassVar[int]
    id: str
    flag: str
    owner: str
    manufacturer: str
    model: str
    year_built: int
    length_m: float
    tonnage_gt: float
    engine_power_kw: float
    def __init__(self, id: _Optional[str] = ..., flag: _Optional[str] = ..., owner: _Optional[str] = ..., manufacturer: _Optional[str] = ..., model: _Optional[str] = ..., year_built: _Optional[int] = ..., length_m: _Optional[float] = ..., tonnage_gt: _Optional[float] = ..., engine_power_kw: _Optional[float] = ...) -> None: ...

class NavigationComponent(_message.Message):
    __slots__ = ("mode", "armed", "emergency", "waypoint_current", "waypoint_total")
    MODE_FIELD_NUMBER: _ClassVar[int]
    ARMED_FIELD_NUMBER: _ClassVar[int]
    EMERGENCY_FIELD_NUMBER: _ClassVar[int]
    WAYPOINT_CURRENT_FIELD_NUMBER: _ClassVar[int]
    WAYPOINT_TOTAL_FIELD_NUMBER: _ClassVar[int]
    mode: NavigationMode
    armed: bool
    emergency: bool
    waypoint_current: int
    waypoint_total: int
    def __init__(self, mode: _Optional[_Union[NavigationMode, str]] = ..., armed: bool = ..., emergency: bool = ..., waypoint_current: _Optional[int] = ..., waypoint_total: _Optional[int] = ...) -> None: ...

class MissionComponent(_message.Message):
    __slots__ = ("members", "description", "destination", "eta")
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    ETA_FIELD_NUMBER: _ClassVar[int]
    members: _containers.RepeatedScalarFieldContainer[str]
    description: str
    destination: str
    eta: _timestamp_pb2.Timestamp
    def __init__(self, members: _Optional[_Iterable[str]] = ..., description: _Optional[str] = ..., destination: _Optional[str] = ..., eta: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class LinkComponent(_message.Message):
    __slots__ = ("status", "rssi_dbm", "snr_db", "via", "last_latency_ms", "avg_latency_ms", "last_seen")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RSSI_DBM_FIELD_NUMBER: _ClassVar[int]
    SNR_DB_FIELD_NUMBER: _ClassVar[int]
    VIA_FIELD_NUMBER: _ClassVar[int]
    LAST_LATENCY_MS_FIELD_NUMBER: _ClassVar[int]
    AVG_LATENCY_MS_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_FIELD_NUMBER: _ClassVar[int]
    status: LinkStatus
    rssi_dbm: int
    snr_db: int
    via: str
    last_latency_ms: int
    avg_latency_ms: int
    last_seen: _timestamp_pb2.Timestamp
    def __init__(self, status: _Optional[_Union[LinkStatus, str]] = ..., rssi_dbm: _Optional[int] = ..., snr_db: _Optional[int] = ..., via: _Optional[str] = ..., last_latency_ms: _Optional[int] = ..., avg_latency_ms: _Optional[int] = ..., last_seen: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CaptureComponent(_message.Message):
    __slots__ = ("payload", "port", "content_type", "captured_by", "captured_at")
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CAPTURED_BY_FIELD_NUMBER: _ClassVar[int]
    CAPTURED_AT_FIELD_NUMBER: _ClassVar[int]
    payload: bytes
    port: int
    content_type: str
    captured_by: str
    captured_at: _timestamp_pb2.Timestamp
    def __init__(self, payload: _Optional[bytes] = ..., port: _Optional[int] = ..., content_type: _Optional[str] = ..., captured_by: _Optional[str] = ..., captured_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PowerComponent(_message.Message):
    __slots__ = ("battery_charge_remaining", "voltage", "remaining_seconds")
    BATTERY_CHARGE_REMAINING_FIELD_NUMBER: _ClassVar[int]
    VOLTAGE_FIELD_NUMBER: _ClassVar[int]
    REMAINING_SECONDS_FIELD_NUMBER: _ClassVar[int]
    battery_charge_remaining: float
    voltage: float
    remaining_seconds: int
    def __init__(self, battery_charge_remaining: _Optional[float] = ..., voltage: _Optional[float] = ..., remaining_seconds: _Optional[int] = ...) -> None: ...

class DeviceClassOption(_message.Message):
    __slots__ = ("label",)
    CLASS_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    label: str
    def __init__(self, label: _Optional[str] = ..., **kwargs) -> None: ...

class ConfigurableComponent(_message.Message):
    __slots__ = ("schema", "value", "state", "error", "label", "applied_version", "supported_device_classes", "scheduled_at")
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    APPLIED_VERSION_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_DEVICE_CLASSES_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_AT_FIELD_NUMBER: _ClassVar[int]
    schema: _struct_pb2.Struct
    value: _struct_pb2.Struct
    state: ConfigurableState
    error: str
    label: str
    applied_version: int
    supported_device_classes: _containers.RepeatedCompositeFieldContainer[DeviceClassOption]
    scheduled_at: _timestamp_pb2.Timestamp
    def __init__(self, schema: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., value: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., state: _Optional[_Union[ConfigurableState, str]] = ..., error: _Optional[str] = ..., label: _Optional[str] = ..., applied_version: _Optional[int] = ..., supported_device_classes: _Optional[_Iterable[_Union[DeviceClassOption, _Mapping]]] = ..., scheduled_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DeviceComponent(_message.Message):
    __slots__ = ("parent", "composition", "unique_hardware_id", "state", "error", "category", "node", "usb", "ip", "serial", "ethernet", "lpwan")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COMPOSITION_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_HARDWARE_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    USB_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    ETHERNET_FIELD_NUMBER: _ClassVar[int]
    LPWAN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    composition: _containers.RepeatedScalarFieldContainer[str]
    unique_hardware_id: str
    state: DeviceState
    error: str
    category: str
    node: NodeDevice
    usb: UsbDevice
    ip: IpDevice
    serial: SerialDevice
    ethernet: EthernetDevice
    lpwan: LPWANDevice
    def __init__(self, parent: _Optional[str] = ..., composition: _Optional[_Iterable[str]] = ..., unique_hardware_id: _Optional[str] = ..., state: _Optional[_Union[DeviceState, str]] = ..., error: _Optional[str] = ..., category: _Optional[str] = ..., node: _Optional[_Union[NodeDevice, _Mapping]] = ..., usb: _Optional[_Union[UsbDevice, _Mapping]] = ..., ip: _Optional[_Union[IpDevice, _Mapping]] = ..., serial: _Optional[_Union[SerialDevice, _Mapping]] = ..., ethernet: _Optional[_Union[EthernetDevice, _Mapping]] = ..., lpwan: _Optional[_Union[LPWANDevice, _Mapping]] = ..., **kwargs) -> None: ...

class NodeDevice(_message.Message):
    __slots__ = ("hostname", "os", "arch", "num_cpu")
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    ARCH_FIELD_NUMBER: _ClassVar[int]
    NUM_CPU_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    os: str
    arch: str
    num_cpu: int
    def __init__(self, hostname: _Optional[str] = ..., os: _Optional[str] = ..., arch: _Optional[str] = ..., num_cpu: _Optional[int] = ...) -> None: ...

class UsbDevice(_message.Message):
    __slots__ = ("vendor_id", "product_id", "device_class", "device_subclass", "device_protocol", "manufacturer_name", "product_name", "serial_number")
    VENDOR_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CLASS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SUBCLASS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    vendor_id: int
    product_id: int
    device_class: int
    device_subclass: int
    device_protocol: int
    manufacturer_name: str
    product_name: str
    serial_number: str
    def __init__(self, vendor_id: _Optional[int] = ..., product_id: _Optional[int] = ..., device_class: _Optional[int] = ..., device_subclass: _Optional[int] = ..., device_protocol: _Optional[int] = ..., manufacturer_name: _Optional[str] = ..., product_name: _Optional[str] = ..., serial_number: _Optional[str] = ...) -> None: ...

class IpDevice(_message.Message):
    __slots__ = ("host", "port")
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    def __init__(self, host: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class EthernetDevice(_message.Message):
    __slots__ = ("mac_address", "vendor")
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    mac_address: str
    vendor: str
    def __init__(self, mac_address: _Optional[str] = ..., vendor: _Optional[str] = ...) -> None: ...

class SerialDevice(_message.Message):
    __slots__ = ("path", "baud_rate")
    PATH_FIELD_NUMBER: _ClassVar[int]
    BAUD_RATE_FIELD_NUMBER: _ClassVar[int]
    path: str
    baud_rate: int
    def __init__(self, path: _Optional[str] = ..., baud_rate: _Optional[int] = ...) -> None: ...

class LPWANDevice(_message.Message):
    __slots__ = ("eui", "address")
    EUI_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    eui: str
    address: str
    def __init__(self, eui: _Optional[str] = ..., address: _Optional[str] = ...) -> None: ...

class ConfigurationComponent(_message.Message):
    __slots__ = ("value", "version")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    value: _struct_pb2.Struct
    version: int
    def __init__(self, value: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., version: _Optional[int] = ...) -> None: ...

class EntityFilter(_message.Message):
    __slots__ = ("id", "label", "geo", "taskable", "component", "controller", "track", "mission", "device", "config")
    ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    GEO_FIELD_NUMBER: _ClassVar[int]
    TASKABLE_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    TRACK_FIELD_NUMBER: _ClassVar[int]
    MISSION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    OR_FIELD_NUMBER: _ClassVar[int]
    NOT_FIELD_NUMBER: _ClassVar[int]
    id: str
    label: str
    geo: GeoFilter
    taskable: TaskableFilter
    component: _containers.RepeatedScalarFieldContainer[int]
    controller: ControllerFilter
    track: TrackFilter
    mission: MissionFilter
    device: DeviceFilter
    config: ConfigurationFilter
    def __init__(self, id: _Optional[str] = ..., label: _Optional[str] = ..., geo: _Optional[_Union[GeoFilter, _Mapping]] = ..., taskable: _Optional[_Union[TaskableFilter, _Mapping]] = ..., component: _Optional[_Iterable[int]] = ..., controller: _Optional[_Union[ControllerFilter, _Mapping]] = ..., track: _Optional[_Union[TrackFilter, _Mapping]] = ..., mission: _Optional[_Union[MissionFilter, _Mapping]] = ..., device: _Optional[_Union[DeviceFilter, _Mapping]] = ..., config: _Optional[_Union[ConfigurationFilter, _Mapping]] = ..., **kwargs) -> None: ...

class ControllerFilter(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class TrackFilter(_message.Message):
    __slots__ = ("tracker",)
    TRACKER_FIELD_NUMBER: _ClassVar[int]
    tracker: str
    def __init__(self, tracker: _Optional[str] = ...) -> None: ...

class MissionFilter(_message.Message):
    __slots__ = ("mission_id", "member_id")
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    mission_id: str
    member_id: str
    def __init__(self, mission_id: _Optional[str] = ..., member_id: _Optional[str] = ...) -> None: ...

class TaskableFilter(_message.Message):
    __slots__ = ("context", "assignee")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEE_FIELD_NUMBER: _ClassVar[int]
    context: TaskableContext
    assignee: TaskableAssignee
    def __init__(self, context: _Optional[_Union[TaskableContext, _Mapping]] = ..., assignee: _Optional[_Union[TaskableAssignee, _Mapping]] = ...) -> None: ...

class GeoFilter(_message.Message):
    __slots__ = ("geometry", "geoEntityId")
    GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    GEOENTITYID_FIELD_NUMBER: _ClassVar[int]
    geometry: Geometry
    geoEntityId: str
    def __init__(self, geometry: _Optional[_Union[Geometry, _Mapping]] = ..., geoEntityId: _Optional[str] = ...) -> None: ...

class DeviceFilter(_message.Message):
    __slots__ = ("parent", "unique_hardware_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_HARDWARE_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    unique_hardware_id: str
    def __init__(self, parent: _Optional[str] = ..., unique_hardware_id: _Optional[str] = ...) -> None: ...

class ConfigurationFilter(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WatchBehavior(_message.Message):
    __slots__ = ("max_rate_hz", "min_priority", "keepalive_interval_ms")
    MAX_RATE_HZ_FIELD_NUMBER: _ClassVar[int]
    MIN_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    KEEPALIVE_INTERVAL_MS_FIELD_NUMBER: _ClassVar[int]
    max_rate_hz: float
    min_priority: Priority
    keepalive_interval_ms: int
    def __init__(self, max_rate_hz: _Optional[float] = ..., min_priority: _Optional[_Union[Priority, str]] = ..., keepalive_interval_ms: _Optional[int] = ...) -> None: ...

class ListEntitiesRequest(_message.Message):
    __slots__ = ("filter", "behaviour")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    BEHAVIOUR_FIELD_NUMBER: _ClassVar[int]
    filter: EntityFilter
    behaviour: WatchBehavior
    def __init__(self, filter: _Optional[_Union[EntityFilter, _Mapping]] = ..., behaviour: _Optional[_Union[WatchBehavior, _Mapping]] = ...) -> None: ...

class ListEntitiesResponse(_message.Message):
    __slots__ = ("entities",)
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[Entity]
    def __init__(self, entities: _Optional[_Iterable[_Union[Entity, _Mapping]]] = ...) -> None: ...

class EntityChangeRequest(_message.Message):
    __slots__ = ("changes", "replacements")
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    REPLACEMENTS_FIELD_NUMBER: _ClassVar[int]
    changes: _containers.RepeatedCompositeFieldContainer[Entity]
    replacements: _containers.RepeatedCompositeFieldContainer[Entity]
    def __init__(self, changes: _Optional[_Iterable[_Union[Entity, _Mapping]]] = ..., replacements: _Optional[_Iterable[_Union[Entity, _Mapping]]] = ...) -> None: ...

class ExpireEntityRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ExpireEntityResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EntityChangeResponse(_message.Message):
    __slots__ = ("accepted", "debug")
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    DEBUG_FIELD_NUMBER: _ClassVar[int]
    accepted: bool
    debug: str
    def __init__(self, accepted: bool = ..., debug: _Optional[str] = ...) -> None: ...

class EntityChangeEvent(_message.Message):
    __slots__ = ("entity", "t")
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    T_FIELD_NUMBER: _ClassVar[int]
    entity: Entity
    t: EntityChange
    def __init__(self, entity: _Optional[_Union[Entity, _Mapping]] = ..., t: _Optional[_Union[EntityChange, str]] = ...) -> None: ...

class EntityChangeBatch(_message.Message):
    __slots__ = ("events",)
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[EntityChangeEvent]
    def __init__(self, events: _Optional[_Iterable[_Union[EntityChangeEvent, _Mapping]]] = ...) -> None: ...

class GetEntityRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetEntityResponse(_message.Message):
    __slots__ = ("entity",)
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: Entity
    def __init__(self, entity: _Optional[_Union[Entity, _Mapping]] = ...) -> None: ...

class GetLocalNodeRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetLocalNodeResponse(_message.Message):
    __slots__ = ("entity", "node_id")
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    entity: Entity
    node_id: str
    def __init__(self, entity: _Optional[_Union[Entity, _Mapping]] = ..., node_id: _Optional[str] = ...) -> None: ...

class ObserverRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ObserverState(_message.Message):
    __slots__ = ("geo", "viewHistory")
    GEO_FIELD_NUMBER: _ClassVar[int]
    VIEWHISTORY_FIELD_NUMBER: _ClassVar[int]
    geo: Geometry
    viewHistory: _timestamp_pb2.Timestamp
    def __init__(self, geo: _Optional[_Union[Geometry, _Mapping]] = ..., viewHistory: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class RunTaskRequest(_message.Message):
    __slots__ = ("entityId",)
    ENTITYID_FIELD_NUMBER: _ClassVar[int]
    entityId: str
    def __init__(self, entityId: _Optional[str] = ...) -> None: ...

class RunTaskResponse(_message.Message):
    __slots__ = ("executionId", "status", "humanReadableReason")
    EXECUTIONID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HUMANREADABLEREASON_FIELD_NUMBER: _ClassVar[int]
    executionId: str
    status: TaskStatus
    humanReadableReason: str
    def __init__(self, executionId: _Optional[str] = ..., status: _Optional[_Union[TaskStatus, str]] = ..., humanReadableReason: _Optional[str] = ...) -> None: ...
