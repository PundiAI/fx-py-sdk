from fxpysdk.fxsdk.x.cosmos.base.query.v1beta1 import pagination_pb2 as _pagination_pb2
from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.api import annotations_pb2 as _annotations_pb2
from fxpysdk.fxsdk.x.cosmos.slashing.v1beta1 import slashing_pb2 as _slashing_pb2
from fxpysdk.fxsdk.x.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryParamsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryParamsResponse(_message.Message):
    __slots__ = ["params"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _slashing_pb2.Params
    def __init__(self, params: _Optional[_Union[_slashing_pb2.Params, _Mapping]] = ...) -> None: ...

class QuerySigningInfoRequest(_message.Message):
    __slots__ = ["cons_address"]
    CONS_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    cons_address: str
    def __init__(self, cons_address: _Optional[str] = ...) -> None: ...

class QuerySigningInfoResponse(_message.Message):
    __slots__ = ["val_signing_info"]
    VAL_SIGNING_INFO_FIELD_NUMBER: _ClassVar[int]
    val_signing_info: _slashing_pb2.ValidatorSigningInfo
    def __init__(self, val_signing_info: _Optional[_Union[_slashing_pb2.ValidatorSigningInfo, _Mapping]] = ...) -> None: ...

class QuerySigningInfosRequest(_message.Message):
    __slots__ = ["pagination"]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.PageRequest
    def __init__(self, pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QuerySigningInfosResponse(_message.Message):
    __slots__ = ["info", "pagination"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    info: _containers.RepeatedCompositeFieldContainer[_slashing_pb2.ValidatorSigningInfo]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, info: _Optional[_Iterable[_Union[_slashing_pb2.ValidatorSigningInfo, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...
