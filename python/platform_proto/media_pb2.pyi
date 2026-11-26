import components_pb2 as _components_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PictureFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PictureFormatUnspecified: _ClassVar[PictureFormat]
    PictureFormatJpeg: _ClassVar[PictureFormat]
    PictureFormatYCbCr420: _ClassVar[PictureFormat]
PictureFormatUnspecified: PictureFormat
PictureFormatJpeg: PictureFormat
PictureFormatYCbCr420: PictureFormat

class GrabFrameRequest(_message.Message):
    __slots__ = ("entity_id", "component", "after", "wait_ms", "format", "max_width")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    WAIT_MS_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    MAX_WIDTH_FIELD_NUMBER: _ClassVar[int]
    entity_id: str
    component: _components_pb2.EntityComponent
    after: _timestamp_pb2.Timestamp
    wait_ms: int
    format: PictureFormat
    max_width: int
    def __init__(self, entity_id: _Optional[str] = ..., component: _Optional[_Union[_components_pb2.EntityComponent, str]] = ..., after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., wait_ms: _Optional[int] = ..., format: _Optional[_Union[PictureFormat, str]] = ..., max_width: _Optional[int] = ...) -> None: ...

class GrabFrameResponse(_message.Message):
    __slots__ = ("frame", "width", "height", "jpeg", "ycbcr420")
    FRAME_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    JPEG_FIELD_NUMBER: _ClassVar[int]
    YCBCR420_FIELD_NUMBER: _ClassVar[int]
    frame: _components_pb2.Reference
    width: int
    height: int
    jpeg: bytes
    ycbcr420: YCbCr420
    def __init__(self, frame: _Optional[_Union[_components_pb2.Reference, _Mapping]] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., jpeg: _Optional[bytes] = ..., ycbcr420: _Optional[_Union[YCbCr420, _Mapping]] = ...) -> None: ...

class YCbCr420(_message.Message):
    __slots__ = ("y", "cb", "cr")
    Y_FIELD_NUMBER: _ClassVar[int]
    CB_FIELD_NUMBER: _ClassVar[int]
    CR_FIELD_NUMBER: _ClassVar[int]
    y: bytes
    cb: bytes
    cr: bytes
    def __init__(self, y: _Optional[bytes] = ..., cb: _Optional[bytes] = ..., cr: _Optional[bytes] = ...) -> None: ...
