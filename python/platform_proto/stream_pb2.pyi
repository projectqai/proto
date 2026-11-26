import components_pb2 as _components_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
import world_pb2 as _world_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamScope(_message.Message):
    __slots__ = ("entity_id", "component")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    entity_id: str
    component: _components_pb2.EntityComponent
    def __init__(self, entity_id: _Optional[str] = ..., component: _Optional[_Union[_components_pb2.EntityComponent, str]] = ...) -> None: ...

class OpenStream(_message.Message):
    __slots__ = ("read", "write", "skip_retained", "buffer", "heartbeat_interval_ms")
    READ_FIELD_NUMBER: _ClassVar[int]
    WRITE_FIELD_NUMBER: _ClassVar[int]
    SKIP_RETAINED_FIELD_NUMBER: _ClassVar[int]
    BUFFER_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_INTERVAL_MS_FIELD_NUMBER: _ClassVar[int]
    read: _containers.RepeatedCompositeFieldContainer[StreamScope]
    write: _containers.RepeatedCompositeFieldContainer[StreamScope]
    skip_retained: bool
    buffer: int
    heartbeat_interval_ms: int
    def __init__(self, read: _Optional[_Iterable[_Union[StreamScope, _Mapping]]] = ..., write: _Optional[_Iterable[_Union[StreamScope, _Mapping]]] = ..., skip_retained: bool = ..., buffer: _Optional[int] = ..., heartbeat_interval_ms: _Optional[int] = ...) -> None: ...

class StreamWriteRequest(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[_world_pb2.Entity]
    def __init__(self, values: _Optional[_Iterable[_Union[_world_pb2.Entity, _Mapping]]] = ...) -> None: ...

class StreamWriteResponse(_message.Message):
    __slots__ = ("fresh",)
    FRESH_FIELD_NUMBER: _ClassVar[int]
    fresh: _containers.RepeatedCompositeFieldContainer[_timestamp_pb2.Timestamp]
    def __init__(self, fresh: _Optional[_Iterable[_Union[_timestamp_pb2.Timestamp, _Mapping]]] = ...) -> None: ...

class StreamOpened(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StreamRequest(_message.Message):
    __slots__ = ("open", "write")
    OPEN_FIELD_NUMBER: _ClassVar[int]
    WRITE_FIELD_NUMBER: _ClassVar[int]
    open: OpenStream
    write: StreamWriteRequest
    def __init__(self, open: _Optional[_Union[OpenStream, _Mapping]] = ..., write: _Optional[_Union[StreamWriteRequest, _Mapping]] = ...) -> None: ...

class StreamResponse(_message.Message):
    __slots__ = ("opened", "ack", "values")
    OPENED_FIELD_NUMBER: _ClassVar[int]
    ACK_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    opened: StreamOpened
    ack: StreamWriteResponse
    values: StreamReadResponse
    def __init__(self, opened: _Optional[_Union[StreamOpened, _Mapping]] = ..., ack: _Optional[_Union[StreamWriteResponse, _Mapping]] = ..., values: _Optional[_Union[StreamReadResponse, _Mapping]] = ...) -> None: ...

class StreamReadResponse(_message.Message):
    __slots__ = ("values", "missed")
    VALUES_FIELD_NUMBER: _ClassVar[int]
    MISSED_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[_world_pb2.Entity]
    missed: int
    def __init__(self, values: _Optional[_Iterable[_Union[_world_pb2.Entity, _Mapping]]] = ..., missed: _Optional[int] = ...) -> None: ...
