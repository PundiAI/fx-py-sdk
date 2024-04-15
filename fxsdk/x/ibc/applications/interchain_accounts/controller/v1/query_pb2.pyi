from fxpysdk.fxsdk.x.ibc.applications.interchain_accounts.controller.v1 import controller_pb2 as _controller_pb2
from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryInterchainAccountRequest(_message.Message):
    __slots__ = ["owner", "connection_id"]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    owner: str
    connection_id: str
    def __init__(self, owner: _Optional[str] = ..., connection_id: _Optional[str] = ...) -> None: ...

class QueryInterchainAccountResponse(_message.Message):
    __slots__ = ["address"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...

class QueryParamsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryParamsResponse(_message.Message):
    __slots__ = ["params"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _controller_pb2.Params
    def __init__(self, params: _Optional[_Union[_controller_pb2.Params, _Mapping]] = ...) -> None: ...
