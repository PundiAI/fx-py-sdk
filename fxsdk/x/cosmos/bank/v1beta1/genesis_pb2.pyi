from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from fxsdk.x.cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from fxsdk.x.cosmos.bank.v1beta1 import bank_pb2 as _bank_pb2
from fxsdk.x.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ["params", "balances", "supply", "denom_metadata"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    BALANCES_FIELD_NUMBER: _ClassVar[int]
    SUPPLY_FIELD_NUMBER: _ClassVar[int]
    DENOM_METADATA_FIELD_NUMBER: _ClassVar[int]
    params: _bank_pb2.Params
    balances: _containers.RepeatedCompositeFieldContainer[Balance]
    supply: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    denom_metadata: _containers.RepeatedCompositeFieldContainer[_bank_pb2.Metadata]
    def __init__(self, params: _Optional[_Union[_bank_pb2.Params, _Mapping]] = ..., balances: _Optional[_Iterable[_Union[Balance, _Mapping]]] = ..., supply: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ..., denom_metadata: _Optional[_Iterable[_Union[_bank_pb2.Metadata, _Mapping]]] = ...) -> None: ...

class Balance(_message.Message):
    __slots__ = ["address", "coins"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    COINS_FIELD_NUMBER: _ClassVar[int]
    address: str
    coins: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    def __init__(self, address: _Optional[str] = ..., coins: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ...) -> None: ...
