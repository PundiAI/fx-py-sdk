from fx.erc20.v1 import erc20_pb2 as _erc20_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ["params", "token_pairs"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_PAIRS_FIELD_NUMBER: _ClassVar[int]
    params: Params
    token_pairs: _containers.RepeatedCompositeFieldContainer[_erc20_pb2.TokenPair]
    def __init__(self, params: _Optional[_Union[Params, _Mapping]] = ..., token_pairs: _Optional[_Iterable[_Union[_erc20_pb2.TokenPair, _Mapping]]] = ...) -> None: ...

class Params(_message.Message):
    __slots__ = ["enable_erc20", "enable_evm_hook", "ibc_timeout"]
    ENABLE_ERC20_FIELD_NUMBER: _ClassVar[int]
    ENABLE_EVM_HOOK_FIELD_NUMBER: _ClassVar[int]
    IBC_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    enable_erc20: bool
    enable_evm_hook: bool
    ibc_timeout: _duration_pb2.Duration
    def __init__(self, enable_erc20: bool = ..., enable_evm_hook: bool = ..., ibc_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
