import components_pb2 as _components_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
import metrics_pb2 as _metrics_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ImagePixelFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ImagePixelFormatUnspecified: _ClassVar[ImagePixelFormat]
    ImagePixelFormatRGB: _ClassVar[ImagePixelFormat]
    ImagePixelFormatBGR: _ClassVar[ImagePixelFormat]
    ImagePixelFormatRGBA: _ClassVar[ImagePixelFormat]
    ImagePixelFormatRGBX: _ClassVar[ImagePixelFormat]
    ImagePixelFormatBGRA: _ClassVar[ImagePixelFormat]
    ImagePixelFormatBGRX: _ClassVar[ImagePixelFormat]
    ImagePixelFormatGRAY8: _ClassVar[ImagePixelFormat]
    ImagePixelFormatI420: _ClassVar[ImagePixelFormat]
    ImagePixelFormatNV12: _ClassVar[ImagePixelFormat]

class SampleFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SampleFormatUnspecified: _ClassVar[SampleFormat]
    SampleFormatU8: _ClassVar[SampleFormat]
    SampleFormatS16: _ClassVar[SampleFormat]
    SampleFormatS32: _ClassVar[SampleFormat]
    SampleFormatF32: _ClassVar[SampleFormat]
    SampleFormatU8Planar: _ClassVar[SampleFormat]
    SampleFormatS16Planar: _ClassVar[SampleFormat]
    SampleFormatS32Planar: _ClassVar[SampleFormat]
    SampleFormatF32Planar: _ClassVar[SampleFormat]

class ImageMaskEncoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ImageMaskEncodingUnspecified: _ClassVar[ImageMaskEncoding]
    ImageMaskEncodingBitmap: _ClassVar[ImageMaskEncoding]
ImagePixelFormatUnspecified: ImagePixelFormat
ImagePixelFormatRGB: ImagePixelFormat
ImagePixelFormatBGR: ImagePixelFormat
ImagePixelFormatRGBA: ImagePixelFormat
ImagePixelFormatRGBX: ImagePixelFormat
ImagePixelFormatBGRA: ImagePixelFormat
ImagePixelFormatBGRX: ImagePixelFormat
ImagePixelFormatGRAY8: ImagePixelFormat
ImagePixelFormatI420: ImagePixelFormat
ImagePixelFormatNV12: ImagePixelFormat
SampleFormatUnspecified: SampleFormat
SampleFormatU8: SampleFormat
SampleFormatS16: SampleFormat
SampleFormatS32: SampleFormat
SampleFormatF32: SampleFormat
SampleFormatU8Planar: SampleFormat
SampleFormatS16Planar: SampleFormat
SampleFormatS32Planar: SampleFormat
SampleFormatF32Planar: SampleFormat
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
    __slots__ = ("pixels", "codec", "width", "height", "data")
    PIXELS_FIELD_NUMBER: _ClassVar[int]
    CODEC_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    pixels: ImagePixels
    codec: ImageCodec
    width: int
    height: int
    data: bytes
    def __init__(self, pixels: _Optional[_Union[ImagePixels, _Mapping]] = ..., codec: _Optional[_Union[ImageCodec, _Mapping]] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class ImageCodec(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: str
    def __init__(self, type: _Optional[str] = ...) -> None: ...

class ImagePixels(_message.Message):
    __slots__ = ("format", "strides", "offsets")
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    STRIDES_FIELD_NUMBER: _ClassVar[int]
    OFFSETS_FIELD_NUMBER: _ClassVar[int]
    format: ImagePixelFormat
    strides: _containers.RepeatedScalarFieldContainer[int]
    offsets: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, format: _Optional[_Union[ImagePixelFormat, str]] = ..., strides: _Optional[_Iterable[int]] = ..., offsets: _Optional[_Iterable[int]] = ...) -> None: ...

class AudioComponent(_message.Message):
    __slots__ = ("pcm", "codec", "sample_rate", "channels", "channel_names", "full_scale_db_spl")
    PCM_FIELD_NUMBER: _ClassVar[int]
    CODEC_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_NAMES_FIELD_NUMBER: _ClassVar[int]
    FULL_SCALE_DB_SPL_FIELD_NUMBER: _ClassVar[int]
    pcm: AudioPcm
    codec: AudioCodec
    sample_rate: int
    channels: int
    channel_names: _containers.RepeatedScalarFieldContainer[str]
    full_scale_db_spl: float
    def __init__(self, pcm: _Optional[_Union[AudioPcm, _Mapping]] = ..., codec: _Optional[_Union[AudioCodec, _Mapping]] = ..., sample_rate: _Optional[int] = ..., channels: _Optional[int] = ..., channel_names: _Optional[_Iterable[str]] = ..., full_scale_db_spl: _Optional[float] = ...) -> None: ...

class AudioPcm(_message.Message):
    __slots__ = ("format", "valid_bits")
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    VALID_BITS_FIELD_NUMBER: _ClassVar[int]
    format: SampleFormat
    valid_bits: int
    def __init__(self, format: _Optional[_Union[SampleFormat, str]] = ..., valid_bits: _Optional[int] = ...) -> None: ...

class AudioCodec(_message.Message):
    __slots__ = ("codec", "description")
    CODEC_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    codec: str
    description: bytes
    def __init__(self, codec: _Optional[str] = ..., description: _Optional[bytes] = ...) -> None: ...

class AudioFrameComponent(_message.Message):
    __slots__ = ("data", "samples")
    DATA_FIELD_NUMBER: _ClassVar[int]
    SAMPLES_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    samples: int
    def __init__(self, data: _Optional[bytes] = ..., samples: _Optional[int] = ...) -> None: ...

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
