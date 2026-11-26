from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor
BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
behavior: _descriptor.FieldDescriptor
MERGE_KEY_FIELD_NUMBER: _ClassVar[int]
merge_key: _descriptor.FieldDescriptor

class ComponentBehavior(_message.Message):
    __slots__ = ("sampled", "managed", "local", "volatile")
    SAMPLED_FIELD_NUMBER: _ClassVar[int]
    MANAGED_FIELD_NUMBER: _ClassVar[int]
    LOCAL_FIELD_NUMBER: _ClassVar[int]
    VOLATILE_FIELD_NUMBER: _ClassVar[int]
    sampled: bool
    managed: bool
    local: bool
    volatile: bool
    def __init__(self, sampled: bool = ..., managed: bool = ..., local: bool = ..., volatile: bool = ...) -> None: ...
