from google.protobuf import any_pb2 as _any_pb2
from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    TYPE_UNSPECIFIED: _ClassVar[Type]
    TYPE_EXECUTE_TX: _ClassVar[Type]
TYPE_UNSPECIFIED: Type
TYPE_EXECUTE_TX: Type

class InterchainAccountPacketData(_message.Message):
    __slots__ = ["type", "data", "memo"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    type: Type
    data: bytes
    memo: str
    def __init__(self, type: _Optional[_Union[Type, str]] = ..., data: _Optional[bytes] = ..., memo: _Optional[str] = ...) -> None: ...

class CosmosTx(_message.Message):
    __slots__ = ["messages"]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, messages: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...
