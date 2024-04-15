from fxsdk.x.cosmos.msg.v1 import msg_pb2 as _msg_pb2
from fxsdk.x.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MsgCallContract(_message.Message):
    __slots__ = ["authority", "contract_address", "data"]
    AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    authority: str
    contract_address: str
    data: str
    def __init__(self, authority: _Optional[str] = ..., contract_address: _Optional[str] = ..., data: _Optional[str] = ...) -> None: ...

class MsgCallContractResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
