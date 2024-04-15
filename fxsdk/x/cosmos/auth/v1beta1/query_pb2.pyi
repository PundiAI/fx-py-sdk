from fxpysdk.fxsdk.x.cosmos.base.query.v1beta1 import pagination_pb2 as _pagination_pb2
from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.api import annotations_pb2 as _annotations_pb2
from fxpysdk.fxsdk.x.cosmos.auth.v1beta1 import auth_pb2 as _auth_pb2
from fxpysdk.fxsdk.x.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryAccountsRequest(_message.Message):
    __slots__ = ["pagination"]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.PageRequest
    def __init__(self, pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryAccountsResponse(_message.Message):
    __slots__ = ["accounts", "pagination"]
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, accounts: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class QueryAccountRequest(_message.Message):
    __slots__ = ["address"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...

class QueryAccountResponse(_message.Message):
    __slots__ = ["account"]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: _any_pb2.Any
    def __init__(self, account: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class QueryParamsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryParamsResponse(_message.Message):
    __slots__ = ["params"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _auth_pb2.Params
    def __init__(self, params: _Optional[_Union[_auth_pb2.Params, _Mapping]] = ...) -> None: ...

class QueryModuleAccountsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryModuleAccountsResponse(_message.Message):
    __slots__ = ["accounts"]
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, accounts: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class QueryModuleAccountByNameRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class QueryModuleAccountByNameResponse(_message.Message):
    __slots__ = ["account"]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: _any_pb2.Any
    def __init__(self, account: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class Bech32PrefixRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Bech32PrefixResponse(_message.Message):
    __slots__ = ["bech32_prefix"]
    BECH32_PREFIX_FIELD_NUMBER: _ClassVar[int]
    bech32_prefix: str
    def __init__(self, bech32_prefix: _Optional[str] = ...) -> None: ...

class AddressBytesToStringRequest(_message.Message):
    __slots__ = ["address_bytes"]
    ADDRESS_BYTES_FIELD_NUMBER: _ClassVar[int]
    address_bytes: bytes
    def __init__(self, address_bytes: _Optional[bytes] = ...) -> None: ...

class AddressBytesToStringResponse(_message.Message):
    __slots__ = ["address_string"]
    ADDRESS_STRING_FIELD_NUMBER: _ClassVar[int]
    address_string: str
    def __init__(self, address_string: _Optional[str] = ...) -> None: ...

class AddressStringToBytesRequest(_message.Message):
    __slots__ = ["address_string"]
    ADDRESS_STRING_FIELD_NUMBER: _ClassVar[int]
    address_string: str
    def __init__(self, address_string: _Optional[str] = ...) -> None: ...

class AddressStringToBytesResponse(_message.Message):
    __slots__ = ["address_bytes"]
    ADDRESS_BYTES_FIELD_NUMBER: _ClassVar[int]
    address_bytes: bytes
    def __init__(self, address_bytes: _Optional[bytes] = ...) -> None: ...

class QueryAccountAddressByIDRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class QueryAccountAddressByIDResponse(_message.Message):
    __slots__ = ["account_address"]
    ACCOUNT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    account_address: str
    def __init__(self, account_address: _Optional[str] = ...) -> None: ...
