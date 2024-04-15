from fxsdk.x.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from fxsdk.x.cosmos.auth.v1beta1 import auth_pb2 as _auth_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InterchainAccount(_message.Message):
    __slots__ = ["base_account", "account_owner"]
    BASE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_OWNER_FIELD_NUMBER: _ClassVar[int]
    base_account: _auth_pb2.BaseAccount
    account_owner: str
    def __init__(self, base_account: _Optional[_Union[_auth_pb2.BaseAccount, _Mapping]] = ..., account_owner: _Optional[str] = ...) -> None: ...
