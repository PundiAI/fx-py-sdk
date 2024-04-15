from google.protobuf import any_pb2 as _any_pb2
from fxpysdk.fxsdk.x.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from fxpysdk.fxsdk.x.cosmos.msg.v1 import msg_pb2 as _msg_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MsgGrantAllowance(_message.Message):
    __slots__ = ["granter", "grantee", "allowance"]
    GRANTER_FIELD_NUMBER: _ClassVar[int]
    GRANTEE_FIELD_NUMBER: _ClassVar[int]
    ALLOWANCE_FIELD_NUMBER: _ClassVar[int]
    granter: str
    grantee: str
    allowance: _any_pb2.Any
    def __init__(self, granter: _Optional[str] = ..., grantee: _Optional[str] = ..., allowance: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class MsgGrantAllowanceResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgRevokeAllowance(_message.Message):
    __slots__ = ["granter", "grantee"]
    GRANTER_FIELD_NUMBER: _ClassVar[int]
    GRANTEE_FIELD_NUMBER: _ClassVar[int]
    granter: str
    grantee: str
    def __init__(self, granter: _Optional[str] = ..., grantee: _Optional[str] = ...) -> None: ...

class MsgRevokeAllowanceResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
