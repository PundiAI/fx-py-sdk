from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Params(_message.Message):
    __slots__ = ["host_enabled", "allow_messages"]
    HOST_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    host_enabled: bool
    allow_messages: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, host_enabled: bool = ..., allow_messages: _Optional[_Iterable[str]] = ...) -> None: ...
