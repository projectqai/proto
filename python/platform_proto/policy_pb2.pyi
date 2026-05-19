from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PolicyAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PolicyActionInvalid: _ClassVar[PolicyAction]
    PolicyActionDeny: _ClassVar[PolicyAction]
    PolicyActionAllow: _ClassVar[PolicyAction]
    PolicyActionLog: _ClassVar[PolicyAction]
    PolicyActionDefer: _ClassVar[PolicyAction]
PolicyActionInvalid: PolicyAction
PolicyActionDeny: PolicyAction
PolicyActionAllow: PolicyAction
PolicyActionLog: PolicyAction
PolicyActionDefer: PolicyAction

class PolicyRule(_message.Message):
    __slots__ = ("action", "cel")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CEL_FIELD_NUMBER: _ClassVar[int]
    action: PolicyAction
    cel: str
    def __init__(self, action: _Optional[_Union[PolicyAction, str]] = ..., cel: _Optional[str] = ...) -> None: ...

class PolicyComponent(_message.Message):
    __slots__ = ("rules",)
    RULES_FIELD_NUMBER: _ClassVar[int]
    rules: _containers.RepeatedCompositeFieldContainer[PolicyRule]
    def __init__(self, rules: _Optional[_Iterable[_Union[PolicyRule, _Mapping]]] = ...) -> None: ...
