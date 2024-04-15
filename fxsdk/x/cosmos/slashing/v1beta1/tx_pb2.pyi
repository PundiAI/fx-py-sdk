from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from fxsdk.x.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from fxsdk.x.cosmos.msg.v1 import msg_pb2 as _msg_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MsgUnjail(_message.Message):
    __slots__ = ["validator_addr"]
    VALIDATOR_ADDR_FIELD_NUMBER: _ClassVar[int]
    validator_addr: str
    def __init__(self, validator_addr: _Optional[str] = ...) -> None: ...

class MsgUnjailResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
