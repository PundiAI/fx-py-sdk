from cosmos.base.query.v1beta1 import pagination_pb2 as _pagination_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.api import annotations_pb2 as _annotations_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from cosmos.bank.v1beta1 import bank_pb2 as _bank_pb2
from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryBalanceRequest(_message.Message):
    __slots__ = ["address", "denom"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    address: str
    denom: str
    def __init__(self, address: _Optional[str] = ..., denom: _Optional[str] = ...) -> None: ...

class QueryBalanceResponse(_message.Message):
    __slots__ = ["balance"]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    balance: _coin_pb2.Coin
    def __init__(self, balance: _Optional[_Union[_coin_pb2.Coin, _Mapping]] = ...) -> None: ...

class QueryAllBalancesRequest(_message.Message):
    __slots__ = ["address", "pagination"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    address: str
    pagination: _pagination_pb2.PageRequest
    def __init__(self, address: _Optional[str] = ..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryAllBalancesResponse(_message.Message):
    __slots__ = ["balances", "pagination"]
    BALANCES_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    balances: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, balances: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class QuerySpendableBalancesRequest(_message.Message):
    __slots__ = ["address", "pagination"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    address: str
    pagination: _pagination_pb2.PageRequest
    def __init__(self, address: _Optional[str] = ..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QuerySpendableBalancesResponse(_message.Message):
    __slots__ = ["balances", "pagination"]
    BALANCES_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    balances: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, balances: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class QueryTotalSupplyRequest(_message.Message):
    __slots__ = ["pagination"]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.PageRequest
    def __init__(self, pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryTotalSupplyResponse(_message.Message):
    __slots__ = ["supply", "pagination"]
    SUPPLY_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    supply: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, supply: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class QuerySupplyOfRequest(_message.Message):
    __slots__ = ["denom"]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    denom: str
    def __init__(self, denom: _Optional[str] = ...) -> None: ...

class QuerySupplyOfResponse(_message.Message):
    __slots__ = ["amount"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    amount: _coin_pb2.Coin
    def __init__(self, amount: _Optional[_Union[_coin_pb2.Coin, _Mapping]] = ...) -> None: ...

class QueryParamsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryParamsResponse(_message.Message):
    __slots__ = ["params"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _bank_pb2.Params
    def __init__(self, params: _Optional[_Union[_bank_pb2.Params, _Mapping]] = ...) -> None: ...

class QueryDenomsMetadataRequest(_message.Message):
    __slots__ = ["pagination"]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.PageRequest
    def __init__(self, pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryDenomsMetadataResponse(_message.Message):
    __slots__ = ["metadatas", "pagination"]
    METADATAS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    metadatas: _containers.RepeatedCompositeFieldContainer[_bank_pb2.Metadata]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, metadatas: _Optional[_Iterable[_Union[_bank_pb2.Metadata, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class QueryDenomMetadataRequest(_message.Message):
    __slots__ = ["denom"]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    denom: str
    def __init__(self, denom: _Optional[str] = ...) -> None: ...

class QueryDenomMetadataResponse(_message.Message):
    __slots__ = ["metadata"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    metadata: _bank_pb2.Metadata
    def __init__(self, metadata: _Optional[_Union[_bank_pb2.Metadata, _Mapping]] = ...) -> None: ...

class QueryDenomOwnersRequest(_message.Message):
    __slots__ = ["denom", "pagination"]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    denom: str
    pagination: _pagination_pb2.PageRequest
    def __init__(self, denom: _Optional[str] = ..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class DenomOwner(_message.Message):
    __slots__ = ["address", "balance"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    address: str
    balance: _coin_pb2.Coin
    def __init__(self, address: _Optional[str] = ..., balance: _Optional[_Union[_coin_pb2.Coin, _Mapping]] = ...) -> None: ...

class QueryDenomOwnersResponse(_message.Message):
    __slots__ = ["denom_owners", "pagination"]
    DENOM_OWNERS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    denom_owners: _containers.RepeatedCompositeFieldContainer[DenomOwner]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, denom_owners: _Optional[_Iterable[_Union[DenomOwner, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...
