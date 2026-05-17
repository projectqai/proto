import geometry_pb2 as _geometry_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TaskableTarget(_message.Message):
    __slots__ = ("position", "waypoints", "entity")
    POSITION_FIELD_NUMBER: _ClassVar[int]
    WAYPOINTS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    position: TaskableTargetPosition
    waypoints: TaskableTargetWaypoints
    entity: TaskableTargetEntity
    def __init__(self, position: _Optional[_Union[TaskableTargetPosition, _Mapping]] = ..., waypoints: _Optional[_Union[TaskableTargetWaypoints, _Mapping]] = ..., entity: _Optional[_Union[TaskableTargetEntity, _Mapping]] = ...) -> None: ...

class TaskableTargetPosition(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TaskableTargetWaypoints(_message.Message):
    __slots__ = ("max", "loop")
    MAX_FIELD_NUMBER: _ClassVar[int]
    LOOP_FIELD_NUMBER: _ClassVar[int]
    max: int
    loop: bool
    def __init__(self, max: _Optional[int] = ..., loop: bool = ...) -> None: ...

class TaskableTargetEntity(_message.Message):
    __slots__ = ("entity", "max")
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    entity: _containers.RepeatedScalarFieldContainer[str]
    max: int
    def __init__(self, entity: _Optional[_Iterable[str]] = ..., max: _Optional[int] = ...) -> None: ...

class TaskExecutionTarget(_message.Message):
    __slots__ = ("position", "waypoints", "entity")
    POSITION_FIELD_NUMBER: _ClassVar[int]
    WAYPOINTS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    position: _geometry_pb2.PlanarPoint
    waypoints: TaskExecutionTargetWaypoints
    entity: TaskExecutionTargetEntity
    def __init__(self, position: _Optional[_Union[_geometry_pb2.PlanarPoint, _Mapping]] = ..., waypoints: _Optional[_Union[TaskExecutionTargetWaypoints, _Mapping]] = ..., entity: _Optional[_Union[TaskExecutionTargetEntity, _Mapping]] = ...) -> None: ...

class TaskExecutionTargetWaypoints(_message.Message):
    __slots__ = ("waypoint",)
    WAYPOINT_FIELD_NUMBER: _ClassVar[int]
    waypoint: _containers.RepeatedCompositeFieldContainer[_geometry_pb2.PlanarPoint]
    def __init__(self, waypoint: _Optional[_Iterable[_Union[_geometry_pb2.PlanarPoint, _Mapping]]] = ...) -> None: ...

class TaskExecutionTargetEntity(_message.Message):
    __slots__ = ("entity",)
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, entity: _Optional[_Iterable[str]] = ...) -> None: ...
