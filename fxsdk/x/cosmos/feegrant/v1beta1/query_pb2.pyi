from cosmos.feegrant.v1beta1 import feegrant_pb2 as _feegrant_pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as _pagination_pb2
from google.api import annotations_pb2 as _annotations_pb2
from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryAllowanceRequest(_message.Message):
    __slots__ = ["granter", "grantee"]
    GRANTER_FIELD_NUMBER: _ClassVar[int]
    GRANTEE_FIELD_NUMBER: _ClassVar[int]
    granter: str
    grantee: str
    def __init__(self, granter: _Optional[str] = ..., grantee: _Optional[str] = ...) -> None: ...

class QueryAllowanceResponse(_message.Message):
    __slots__ = ["allowance"]
    ALLOWANCE_FIELD_NUMBER: _ClassVar[int]
    allowance: _feegrant_pb2.Grant
    def __init__(self, allowance: _Optional[_Union[_feegrant_pb2.Grant, _Mapping]] = ...) -> None: ...

class QueryAllowancesRequest(_message.Message):
    __slots__ = ["grantee", "pagination"]
    GRANTEE_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    grantee: str
    pagination: _pagination_pb2.PageRequest
    def __init__(self, grantee: _Optional[str] = ..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryAllowancesResponse(_message.Message):
    __slots__ = ["allowances", "pagination"]
    ALLOWANCES_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    allowances: _containers.RepeatedCompositeFieldContainer[_feegrant_pb2.Grant]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, allowances: _Optional[_Iterable[_Union[_feegrant_pb2.Grant, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class QueryAllowancesByGranterRequest(_message.Message):
    __slots__ = ["granter", "pagination"]
    GRANTER_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    granter: str
    pagination: _pagination_pb2.PageRequest
    def __init__(self, granter: _Optional[str] = ..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryAllowancesByGranterResponse(_message.Message):
    __slots__ = ["allowances", "pagination"]
    ALLOWANCES_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    allowances: _containers.RepeatedCompositeFieldContainer[_feegrant_pb2.Grant]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, allowances: _Optional[_Iterable[_Union[_feegrant_pb2.Grant, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...
