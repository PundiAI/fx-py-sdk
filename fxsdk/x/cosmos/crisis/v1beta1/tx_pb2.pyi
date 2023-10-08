from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from cosmos.msg.v1 import msg_pb2 as _msg_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MsgVerifyInvariant(_message.Message):
    __slots__ = ["sender", "invariant_module_name", "invariant_route"]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    INVARIANT_MODULE_NAME_FIELD_NUMBER: _ClassVar[int]
    INVARIANT_ROUTE_FIELD_NUMBER: _ClassVar[int]
    sender: str
    invariant_module_name: str
    invariant_route: str
    def __init__(self, sender: _Optional[str] = ..., invariant_module_name: _Optional[str] = ..., invariant_route: _Optional[str] = ...) -> None: ...

class MsgVerifyInvariantResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
