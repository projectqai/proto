import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Priority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PriorityReserved0: _ClassVar[Priority]
    PriorityLow: _ClassVar[Priority]
    PriorityHigh: _ClassVar[Priority]
    PriorityBurst: _ClassVar[Priority]

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
PriorityReserved0: Priority
PriorityLow: Priority
PriorityHigh: Priority
PriorityBurst: Priority
EntityChangeInvalid: EntityChange
EntityChangeUpdated: EntityChange
EntityChangeExpired: EntityChange
EntityChangeUnobserved: EntityChange
TaskStatusInvalid: TaskStatus
TaskStatusRunning: TaskStatus
TaskStatusCompleted: TaskStatus
TaskStatusFailed: TaskStatus

class Entity(_message.Message):
    __slots__ = ("id", "label", "controller", "lifetime", "priority", "geo", "symbol", "camera", "detection", "bearing", "locationUncertainty", "track", "locator", "taskable")
    ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    LIFETIME_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    GEO_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    CAMERA_FIELD_NUMBER: _ClassVar[int]
    DETECTION_FIELD_NUMBER: _ClassVar[int]
    BEARING_FIELD_NUMBER: _ClassVar[int]
    LOCATIONUNCERTAINTY_FIELD_NUMBER: _ClassVar[int]
    TRACK_FIELD_NUMBER: _ClassVar[int]
    LOCATOR_FIELD_NUMBER: _ClassVar[int]
    TASKABLE_FIELD_NUMBER: _ClassVar[int]
    id: str
    label: str
    controller: ControllerRef
    lifetime: Lifetime
    priority: Priority
    geo: GeoSpatialComponent
    symbol: SymbolComponent
    camera: CameraComponent
    detection: DetectionComponent
    bearing: BearingComponent
    locationUncertainty: LocationUncertaintyComponent
    track: TrackComponent
    locator: LocatorComponent
    taskable: TaskableComponent
    def __init__(self, id: _Optional[str] = ..., label: _Optional[str] = ..., controller: _Optional[_Union[ControllerRef, _Mapping]] = ..., lifetime: _Optional[_Union[Lifetime, _Mapping]] = ..., priority: _Optional[_Union[Priority, str]] = ..., geo: _Optional[_Union[GeoSpatialComponent, _Mapping]] = ..., symbol: _Optional[_Union[SymbolComponent, _Mapping]] = ..., camera: _Optional[_Union[CameraComponent, _Mapping]] = ..., detection: _Optional[_Union[DetectionComponent, _Mapping]] = ..., bearing: _Optional[_Union[BearingComponent, _Mapping]] = ..., locationUncertainty: _Optional[_Union[LocationUncertaintyComponent, _Mapping]] = ..., track: _Optional[_Union[TrackComponent, _Mapping]] = ..., locator: _Optional[_Union[LocatorComponent, _Mapping]] = ..., taskable: _Optional[_Union[TaskableComponent, _Mapping]] = ...) -> None: ...

class ControllerRef(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class Lifetime(_message.Message):
    __slots__ = ("until",)
    FROM_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    until: _timestamp_pb2.Timestamp
    def __init__(self, until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., **kwargs) -> None: ...

class GeoSpatialComponent(_message.Message):
    __slots__ = ("longitude", "latitude", "altitude")
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    longitude: float
    latitude: float
    altitude: float
    def __init__(self, longitude: _Optional[float] = ..., latitude: _Optional[float] = ..., altitude: _Optional[float] = ...) -> None: ...

class SymbolComponent(_message.Message):
    __slots__ = ("milStd2525C",)
    MILSTD2525C_FIELD_NUMBER: _ClassVar[int]
    milStd2525C: str
    def __init__(self, milStd2525C: _Optional[str] = ...) -> None: ...

class Camera(_message.Message):
    __slots__ = ("label", "url")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    label: str
    url: str
    def __init__(self, label: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class CameraComponent(_message.Message):
    __slots__ = ("cameras",)
    CAMERAS_FIELD_NUMBER: _ClassVar[int]
    cameras: _containers.RepeatedCompositeFieldContainer[Camera]
    def __init__(self, cameras: _Optional[_Iterable[_Union[Camera, _Mapping]]] = ...) -> None: ...

class DetectionComponent(_message.Message):
    __slots__ = ("detectorEntityID", "classification", "lastMeasured")
    DETECTORENTITYID_FIELD_NUMBER: _ClassVar[int]
    CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    LASTMEASURED_FIELD_NUMBER: _ClassVar[int]
    detectorEntityID: str
    classification: str
    lastMeasured: _timestamp_pb2.Timestamp
    def __init__(self, detectorEntityID: _Optional[str] = ..., classification: _Optional[str] = ..., lastMeasured: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class BearingComponent(_message.Message):
    __slots__ = ("azimuth", "elevation")
    AZIMUTH_FIELD_NUMBER: _ClassVar[int]
    ELEVATION_FIELD_NUMBER: _ClassVar[int]
    azimuth: float
    elevation: float
    def __init__(self, azimuth: _Optional[float] = ..., elevation: _Optional[float] = ...) -> None: ...

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

class LocationUncertaintyComponent(_message.Message):
    __slots__ = ("positionEnuCov", "velocityEnuCov")
    POSITIONENUCOV_FIELD_NUMBER: _ClassVar[int]
    VELOCITYENUCOV_FIELD_NUMBER: _ClassVar[int]
    positionEnuCov: CovarianceMatrix
    velocityEnuCov: CovarianceMatrix
    def __init__(self, positionEnuCov: _Optional[_Union[CovarianceMatrix, _Mapping]] = ..., velocityEnuCov: _Optional[_Union[CovarianceMatrix, _Mapping]] = ...) -> None: ...

class TrackComponent(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LocatorComponent(_message.Message):
    __slots__ = ("locatedEntityID",)
    LOCATEDENTITYID_FIELD_NUMBER: _ClassVar[int]
    locatedEntityID: str
    def __init__(self, locatedEntityID: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("reserved", "label", "context", "assignee")
    RESERVED_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEE_FIELD_NUMBER: _ClassVar[int]
    reserved: str
    label: str
    context: _containers.RepeatedCompositeFieldContainer[TaskableContext]
    assignee: _containers.RepeatedCompositeFieldContainer[TaskableAssignee]
    def __init__(self, reserved: _Optional[str] = ..., label: _Optional[str] = ..., context: _Optional[_Iterable[_Union[TaskableContext, _Mapping]]] = ..., assignee: _Optional[_Iterable[_Union[TaskableAssignee, _Mapping]]] = ...) -> None: ...

class Geometry(_message.Message):
    __slots__ = ("wkb",)
    WKB_FIELD_NUMBER: _ClassVar[int]
    wkb: bytes
    def __init__(self, wkb: _Optional[bytes] = ...) -> None: ...

class ListEntitiesRequest(_message.Message):
    __slots__ = ("geo", "taskableContext", "TaskableAssignee")
    GEO_FIELD_NUMBER: _ClassVar[int]
    TASKABLECONTEXT_FIELD_NUMBER: _ClassVar[int]
    TASKABLEASSIGNEE_FIELD_NUMBER: _ClassVar[int]
    geo: Geometry
    taskableContext: TaskableContext
    TaskableAssignee: TaskableAssignee
    def __init__(self, geo: _Optional[_Union[Geometry, _Mapping]] = ..., taskableContext: _Optional[_Union[TaskableContext, _Mapping]] = ..., TaskableAssignee: _Optional[_Union[TaskableAssignee, _Mapping]] = ...) -> None: ...

class ListEntitiesResponse(_message.Message):
    __slots__ = ("entities",)
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[Entity]
    def __init__(self, entities: _Optional[_Iterable[_Union[Entity, _Mapping]]] = ...) -> None: ...

class EntityChangeRequest(_message.Message):
    __slots__ = ("changes",)
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    changes: _containers.RepeatedCompositeFieldContainer[Entity]
    def __init__(self, changes: _Optional[_Iterable[_Union[Entity, _Mapping]]] = ...) -> None: ...

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

class ObserverRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ObserverState(_message.Message):
    __slots__ = ("geo", "viewHistory")
    GEO_FIELD_NUMBER: _ClassVar[int]
    VIEWHISTORY_FIELD_NUMBER: _ClassVar[int]
    geo: Geometry
    viewHistory: _timestamp_pb2.Timestamp
    def __init__(self, geo: _Optional[_Union[Geometry, _Mapping]] = ..., viewHistory: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

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
