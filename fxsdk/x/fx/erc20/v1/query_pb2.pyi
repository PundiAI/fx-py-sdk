from fxpysdk.fxsdk.x.cosmos.base.query.v1beta1 import pagination_pb2 as _pagination_pb2
from fxpysdk.fxsdk.x.fx.erc20.v1 import erc20_pb2 as _erc20_pb2
from fxpysdk.fxsdk.x.fx.erc20.v1 import genesis_pb2 as _genesis_pb2
from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryTokenPairsRequest(_message.Message):
    __slots__ = ["pagination"]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.PageRequest
    def __init__(self, pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryTokenPairsResponse(_message.Message):
    __slots__ = ["token_pairs", "pagination"]
    TOKEN_PAIRS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    token_pairs: _containers.RepeatedCompositeFieldContainer[_erc20_pb2.TokenPair]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, token_pairs: _Optional[_Iterable[_Union[_erc20_pb2.TokenPair, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class QueryTokenPairRequest(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class QueryTokenPairResponse(_message.Message):
    __slots__ = ["token_pair"]
    TOKEN_PAIR_FIELD_NUMBER: _ClassVar[int]
    token_pair: _erc20_pb2.TokenPair
    def __init__(self, token_pair: _Optional[_Union[_erc20_pb2.TokenPair, _Mapping]] = ...) -> None: ...

class QueryParamsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryParamsResponse(_message.Message):
    __slots__ = ["params"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _genesis_pb2.Params
    def __init__(self, params: _Optional[_Union[_genesis_pb2.Params, _Mapping]] = ...) -> None: ...

class QueryDenomAliasesRequest(_message.Message):
    __slots__ = ["denom"]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    denom: str
    def __init__(self, denom: _Optional[str] = ...) -> None: ...

class QueryDenomAliasesResponse(_message.Message):
    __slots__ = ["aliases"]
    ALIASES_FIELD_NUMBER: _ClassVar[int]
    aliases: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, aliases: _Optional[_Iterable[str]] = ...) -> None: ...

class QueryAliasDenomRequest(_message.Message):
    __slots__ = ["alias"]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    alias: str
    def __init__(self, alias: _Optional[str] = ...) -> None: ...

class QueryAliasDenomResponse(_message.Message):
    __slots__ = ["denom"]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    denom: str
    def __init__(self, denom: _Optional[str] = ...) -> None: ...
