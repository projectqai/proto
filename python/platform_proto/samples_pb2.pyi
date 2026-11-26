import components_pb2 as _components_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
import metrics_pb2 as _metrics_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ImageMaskEncoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ImageMaskEncodingUnspecified: _ClassVar[ImageMaskEncoding]
    ImageMaskEncodingBitmap: _ClassVar[ImageMaskEncoding]
ImageMaskEncodingUnspecified: ImageMaskEncoding
ImageMaskEncodingBitmap: ImageMaskEncoding

class VideoComponent(_message.Message):
    __slots__ = ("codec", "width", "height")
    CODEC_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    codec: str
    width: int
    height: int
    def __init__(self, codec: _Optional[str] = ..., width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class VideoFrameComponent(_message.Message):
    __slots__ = ("body", "keyframe")
    BODY_FIELD_NUMBER: _ClassVar[int]
    KEYFRAME_FIELD_NUMBER: _ClassVar[int]
    body: bytes
    keyframe: bool
    def __init__(self, body: _Optional[bytes] = ..., keyframe: bool = ...) -> None: ...

class ImageComponent(_message.Message):
    __slots__ = ("format", "width", "height", "stride", "data")
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    STRIDE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    format: str
    width: int
    height: int
    stride: int
    data: bytes
    def __init__(self, format: _Optional[str] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., stride: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class WaveformComponent(_message.Message):
    __slots__ = ("format", "sample_rate", "channels", "channel_names", "kind", "unit", "scale", "range")
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_NAMES_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    format: str
    sample_rate: int
    channels: int
    channel_names: _containers.RepeatedScalarFieldContainer[str]
    kind: _metrics_pb2.MetricKind
    unit: _metrics_pb2.MetricUnit
    scale: float
    range: _metrics_pb2.MetricRange
    def __init__(self, format: _Optional[str] = ..., sample_rate: _Optional[int] = ..., channels: _Optional[int] = ..., channel_names: _Optional[_Iterable[str]] = ..., kind: _Optional[_Union[_metrics_pb2.MetricKind, str]] = ..., unit: _Optional[_Union[_metrics_pb2.MetricUnit, str]] = ..., scale: _Optional[float] = ..., range: _Optional[_Union[_metrics_pb2.MetricRange, _Mapping]] = ...) -> None: ...

class WaveformFrameComponent(_message.Message):
    __slots__ = ("data", "scale")
    DATA_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    scale: float
    def __init__(self, data: _Optional[bytes] = ..., scale: _Optional[float] = ...) -> None: ...

class McapChannelComponent(_message.Message):
    __slots__ = ("topic", "message_encoding", "schema_name", "schema_encoding", "schema", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ENCODING_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_ENCODING_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    topic: str
    message_encoding: str
    schema_name: str
    schema_encoding: str
    schema: bytes
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, topic: _Optional[str] = ..., message_encoding: _Optional[str] = ..., schema_name: _Optional[str] = ..., schema_encoding: _Optional[str] = ..., schema: _Optional[bytes] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class McapMessageComponent(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class ImageMask(_message.Message):
    __slots__ = ("x", "y", "width", "height", "encoding", "data")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    x: int
    y: int
    width: int
    height: int
    encoding: ImageMaskEncoding
    data: bytes
    def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., encoding: _Optional[_Union[ImageMaskEncoding, str]] = ..., data: _Optional[bytes] = ...) -> None: ...

class StreamComponent(_message.Message):
    __slots__ = ("streams",)
    class Stream(_message.Message):
        __slots__ = ("component", "last", "readers", "latency_ms")
        COMPONENT_FIELD_NUMBER: _ClassVar[int]
        LAST_FIELD_NUMBER: _ClassVar[int]
        READERS_FIELD_NUMBER: _ClassVar[int]
        LATENCY_MS_FIELD_NUMBER: _ClassVar[int]
        component: _components_pb2.EntityComponent
        last: _timestamp_pb2.Timestamp
        readers: _containers.RepeatedScalarFieldContainer[str]
        latency_ms: int
        def __init__(self, component: _Optional[_Union[_components_pb2.EntityComponent, str]] = ..., last: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., readers: _Optional[_Iterable[str]] = ..., latency_ms: _Optional[int] = ...) -> None: ...
    STREAMS_FIELD_NUMBER: _ClassVar[int]
    streams: _containers.RepeatedCompositeFieldContainer[StreamComponent.Stream]
    def __init__(self, streams: _Optional[_Iterable[_Union[StreamComponent.Stream, _Mapping]]] = ...) -> None: ...
