from google.api import annotations_pb2 as _annotations_pb2
from ibc.applications.interchain_accounts.host.v1 import host_pb2 as _host_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryParamsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryParamsResponse(_message.Message):
    __slots__ = ["params"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _host_pb2.Params
    def __init__(self, params: _Optional[_Union[_host_pb2.Params, _Mapping]] = ...) -> None: ...
