from fxsdk.x.cosmos.bank.v1beta1 import bank_pb2 as _bank_pb2
from fxsdk.x.cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from fxsdk.x.cosmos.msg.v1 import msg_pb2 as _msg_pb2
from fxsdk.x.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from fxsdk.x.fx.erc20.v1 import erc20_pb2 as _erc20_pb2
from fxsdk.x.fx.erc20.v1 import genesis_pb2 as _genesis_pb2
from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MsgConvertCoin(_message.Message):
    __slots__ = ["coin", "receiver", "sender"]
    COIN_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    coin: _coin_pb2.Coin
    receiver: str
    sender: str
    def __init__(self, coin: _Optional[_Union[_coin_pb2.Coin, _Mapping]] = ..., receiver: _Optional[str] = ..., sender: _Optional[str] = ...) -> None: ...

class MsgConvertCoinResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgConvertERC20(_message.Message):
    __slots__ = ["contract_address", "amount", "receiver", "sender"]
    CONTRACT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    contract_address: str
    amount: str
    receiver: str
    sender: str
    def __init__(self, contract_address: _Optional[str] = ..., amount: _Optional[str] = ..., receiver: _Optional[str] = ..., sender: _Optional[str] = ...) -> None: ...

class MsgConvertERC20Response(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgConvertDenom(_message.Message):
    __slots__ = ["sender", "receiver", "coin", "target"]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_FIELD_NUMBER: _ClassVar[int]
    COIN_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    sender: str
    receiver: str
    coin: _coin_pb2.Coin
    target: str
    def __init__(self, sender: _Optional[str] = ..., receiver: _Optional[str] = ..., coin: _Optional[_Union[_coin_pb2.Coin, _Mapping]] = ..., target: _Optional[str] = ...) -> None: ...

class MsgConvertDenomResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgUpdateParams(_message.Message):
    __slots__ = ["authority", "params"]
    AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    authority: str
    params: _genesis_pb2.Params
    def __init__(self, authority: _Optional[str] = ..., params: _Optional[_Union[_genesis_pb2.Params, _Mapping]] = ...) -> None: ...

class MsgUpdateParamsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgRegisterCoin(_message.Message):
    __slots__ = ["authority", "metadata"]
    AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    authority: str
    metadata: _bank_pb2.Metadata
    def __init__(self, authority: _Optional[str] = ..., metadata: _Optional[_Union[_bank_pb2.Metadata, _Mapping]] = ...) -> None: ...

class MsgRegisterCoinResponse(_message.Message):
    __slots__ = ["pair"]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    pair: _erc20_pb2.TokenPair
    def __init__(self, pair: _Optional[_Union[_erc20_pb2.TokenPair, _Mapping]] = ...) -> None: ...

class MsgRegisterERC20(_message.Message):
    __slots__ = ["authority", "erc20address", "aliases"]
    AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    ERC20ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ALIASES_FIELD_NUMBER: _ClassVar[int]
    authority: str
    erc20address: str
    aliases: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, authority: _Optional[str] = ..., erc20address: _Optional[str] = ..., aliases: _Optional[_Iterable[str]] = ...) -> None: ...

class MsgRegisterERC20Response(_message.Message):
    __slots__ = ["pair"]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    pair: _erc20_pb2.TokenPair
    def __init__(self, pair: _Optional[_Union[_erc20_pb2.TokenPair, _Mapping]] = ...) -> None: ...

class MsgToggleTokenConversion(_message.Message):
    __slots__ = ["authority", "token"]
    AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    authority: str
    token: str
    def __init__(self, authority: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class MsgToggleTokenConversionResponse(_message.Message):
    __slots__ = ["pair"]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    pair: _erc20_pb2.TokenPair
    def __init__(self, pair: _Optional[_Union[_erc20_pb2.TokenPair, _Mapping]] = ...) -> None: ...

class MsgUpdateDenomAlias(_message.Message):
    __slots__ = ["authority", "denom", "alias"]
    AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    authority: str
    denom: str
    alias: str
    def __init__(self, authority: _Optional[str] = ..., denom: _Optional[str] = ..., alias: _Optional[str] = ...) -> None: ...

class MsgUpdateDenomAliasResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
