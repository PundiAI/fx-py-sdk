from fxpysdk.fxsdk.x.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import any_pb2 as _any_pb2
from fxpysdk.fxsdk.x.cosmos.authz.v1beta1 import authz_pb2 as _authz_pb2
from fxpysdk.fxsdk.x.cosmos.msg.v1 import msg_pb2 as _msg_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MsgGrant(_message.Message):
    __slots__ = ["granter", "grantee", "grant"]
    GRANTER_FIELD_NUMBER: _ClassVar[int]
    GRANTEE_FIELD_NUMBER: _ClassVar[int]
    GRANT_FIELD_NUMBER: _ClassVar[int]
    granter: str
    grantee: str
    grant: _authz_pb2.Grant
    def __init__(self, granter: _Optional[str] = ..., grantee: _Optional[str] = ..., grant: _Optional[_Union[_authz_pb2.Grant, _Mapping]] = ...) -> None: ...

class MsgExecResponse(_message.Message):
    __slots__ = ["results"]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, results: _Optional[_Iterable[bytes]] = ...) -> None: ...

class MsgExec(_message.Message):
    __slots__ = ["grantee", "msgs"]
    GRANTEE_FIELD_NUMBER: _ClassVar[int]
    MSGS_FIELD_NUMBER: _ClassVar[int]
    grantee: str
    msgs: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, grantee: _Optional[str] = ..., msgs: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class MsgGrantResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgRevoke(_message.Message):
    __slots__ = ["granter", "grantee", "msg_type_url"]
    GRANTER_FIELD_NUMBER: _ClassVar[int]
    GRANTEE_FIELD_NUMBER: _ClassVar[int]
    MSG_TYPE_URL_FIELD_NUMBER: _ClassVar[int]
    granter: str
    grantee: str
    msg_type_url: str
    def __init__(self, granter: _Optional[str] = ..., grantee: _Optional[str] = ..., msg_type_url: _Optional[str] = ...) -> None: ...

class MsgRevokeResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
