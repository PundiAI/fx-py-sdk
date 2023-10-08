from google.api import annotations_pb2 as _annotations_pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as _pagination_pb2
from cosmos.authz.v1beta1 import authz_pb2 as _authz_pb2
from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryGrantsRequest(_message.Message):
    __slots__ = ["granter", "grantee", "msg_type_url", "pagination"]
    GRANTER_FIELD_NUMBER: _ClassVar[int]
    GRANTEE_FIELD_NUMBER: _ClassVar[int]
    MSG_TYPE_URL_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    granter: str
    grantee: str
    msg_type_url: str
    pagination: _pagination_pb2.PageRequest
    def __init__(self, granter: _Optional[str] = ..., grantee: _Optional[str] = ..., msg_type_url: _Optional[str] = ..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryGrantsResponse(_message.Message):
    __slots__ = ["grants", "pagination"]
    GRANTS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    grants: _containers.RepeatedCompositeFieldContainer[_authz_pb2.Grant]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, grants: _Optional[_Iterable[_Union[_authz_pb2.Grant, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class QueryGranterGrantsRequest(_message.Message):
    __slots__ = ["granter", "pagination"]
    GRANTER_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    granter: str
    pagination: _pagination_pb2.PageRequest
    def __init__(self, granter: _Optional[str] = ..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryGranterGrantsResponse(_message.Message):
    __slots__ = ["grants", "pagination"]
    GRANTS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    grants: _containers.RepeatedCompositeFieldContainer[_authz_pb2.GrantAuthorization]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, grants: _Optional[_Iterable[_Union[_authz_pb2.GrantAuthorization, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class QueryGranteeGrantsRequest(_message.Message):
    __slots__ = ["grantee", "pagination"]
    GRANTEE_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    grantee: str
    pagination: _pagination_pb2.PageRequest
    def __init__(self, grantee: _Optional[str] = ..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryGranteeGrantsResponse(_message.Message):
    __slots__ = ["grants", "pagination"]
    GRANTS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    grants: _containers.RepeatedCompositeFieldContainer[_authz_pb2.GrantAuthorization]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, grants: _Optional[_Iterable[_Union[_authz_pb2.GrantAuthorization, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...
