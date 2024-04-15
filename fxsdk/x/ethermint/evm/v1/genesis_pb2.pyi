from fxsdk.x.ethermint.evm.v1 import evm_pb2 as _evm_pb2
from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ["accounts", "params"]
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.RepeatedCompositeFieldContainer[GenesisAccount]
    params: _evm_pb2.Params
    def __init__(self, accounts: _Optional[_Iterable[_Union[GenesisAccount, _Mapping]]] = ..., params: _Optional[_Union[_evm_pb2.Params, _Mapping]] = ...) -> None: ...

class GenesisAccount(_message.Message):
    __slots__ = ["address", "code", "storage"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    address: str
    code: str
    storage: _containers.RepeatedCompositeFieldContainer[_evm_pb2.State]
    def __init__(self, address: _Optional[str] = ..., code: _Optional[str] = ..., storage: _Optional[_Iterable[_Union[_evm_pb2.State, _Mapping]]] = ...) -> None: ...
