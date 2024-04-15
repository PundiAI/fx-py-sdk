from fxsdk.x.cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from fxsdk.x.fx.legacy.gravity.v1 import types_pb2 as _types_pb2
from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MsgValsetConfirm(_message.Message):
    __slots__ = ["nonce", "orchestrator", "eth_address", "signature"]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    ORCHESTRATOR_FIELD_NUMBER: _ClassVar[int]
    ETH_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    nonce: int
    orchestrator: str
    eth_address: str
    signature: str
    def __init__(self, nonce: _Optional[int] = ..., orchestrator: _Optional[str] = ..., eth_address: _Optional[str] = ..., signature: _Optional[str] = ...) -> None: ...

class MsgValsetConfirmResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgSendToEth(_message.Message):
    __slots__ = ["sender", "eth_dest", "amount", "bridge_fee"]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    ETH_DEST_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_FEE_FIELD_NUMBER: _ClassVar[int]
    sender: str
    eth_dest: str
    amount: _coin_pb2.Coin
    bridge_fee: _coin_pb2.Coin
    def __init__(self, sender: _Optional[str] = ..., eth_dest: _Optional[str] = ..., amount: _Optional[_Union[_coin_pb2.Coin, _Mapping]] = ..., bridge_fee: _Optional[_Union[_coin_pb2.Coin, _Mapping]] = ...) -> None: ...

class MsgSendToEthResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgRequestBatch(_message.Message):
    __slots__ = ["sender", "denom", "minimum_fee", "feeReceive", "base_fee"]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_FEE_FIELD_NUMBER: _ClassVar[int]
    FEERECEIVE_FIELD_NUMBER: _ClassVar[int]
    BASE_FEE_FIELD_NUMBER: _ClassVar[int]
    sender: str
    denom: str
    minimum_fee: str
    feeReceive: str
    base_fee: str
    def __init__(self, sender: _Optional[str] = ..., denom: _Optional[str] = ..., minimum_fee: _Optional[str] = ..., feeReceive: _Optional[str] = ..., base_fee: _Optional[str] = ...) -> None: ...

class MsgRequestBatchResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgConfirmBatch(_message.Message):
    __slots__ = ["nonce", "token_contract", "eth_signer", "orchestrator", "signature"]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    ETH_SIGNER_FIELD_NUMBER: _ClassVar[int]
    ORCHESTRATOR_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    nonce: int
    token_contract: str
    eth_signer: str
    orchestrator: str
    signature: str
    def __init__(self, nonce: _Optional[int] = ..., token_contract: _Optional[str] = ..., eth_signer: _Optional[str] = ..., orchestrator: _Optional[str] = ..., signature: _Optional[str] = ...) -> None: ...

class MsgConfirmBatchResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgDepositClaim(_message.Message):
    __slots__ = ["event_nonce", "block_height", "token_contract", "amount", "eth_sender", "fx_receiver", "target_ibc", "orchestrator"]
    EVENT_NONCE_FIELD_NUMBER: _ClassVar[int]
    BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    ETH_SENDER_FIELD_NUMBER: _ClassVar[int]
    FX_RECEIVER_FIELD_NUMBER: _ClassVar[int]
    TARGET_IBC_FIELD_NUMBER: _ClassVar[int]
    ORCHESTRATOR_FIELD_NUMBER: _ClassVar[int]
    event_nonce: int
    block_height: int
    token_contract: str
    amount: str
    eth_sender: str
    fx_receiver: str
    target_ibc: str
    orchestrator: str
    def __init__(self, event_nonce: _Optional[int] = ..., block_height: _Optional[int] = ..., token_contract: _Optional[str] = ..., amount: _Optional[str] = ..., eth_sender: _Optional[str] = ..., fx_receiver: _Optional[str] = ..., target_ibc: _Optional[str] = ..., orchestrator: _Optional[str] = ...) -> None: ...

class MsgDepositClaimResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgWithdrawClaim(_message.Message):
    __slots__ = ["event_nonce", "block_height", "batch_nonce", "token_contract", "orchestrator"]
    EVENT_NONCE_FIELD_NUMBER: _ClassVar[int]
    BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    BATCH_NONCE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    ORCHESTRATOR_FIELD_NUMBER: _ClassVar[int]
    event_nonce: int
    block_height: int
    batch_nonce: int
    token_contract: str
    orchestrator: str
    def __init__(self, event_nonce: _Optional[int] = ..., block_height: _Optional[int] = ..., batch_nonce: _Optional[int] = ..., token_contract: _Optional[str] = ..., orchestrator: _Optional[str] = ...) -> None: ...

class MsgWithdrawClaimResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgCancelSendToEth(_message.Message):
    __slots__ = ["transaction_id", "sender"]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    transaction_id: int
    sender: str
    def __init__(self, transaction_id: _Optional[int] = ..., sender: _Optional[str] = ...) -> None: ...

class MsgCancelSendToEthResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgValsetUpdatedClaim(_message.Message):
    __slots__ = ["event_nonce", "block_height", "valset_nonce", "members", "orchestrator"]
    EVENT_NONCE_FIELD_NUMBER: _ClassVar[int]
    BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    VALSET_NONCE_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    ORCHESTRATOR_FIELD_NUMBER: _ClassVar[int]
    event_nonce: int
    block_height: int
    valset_nonce: int
    members: _containers.RepeatedCompositeFieldContainer[_types_pb2.BridgeValidator]
    orchestrator: str
    def __init__(self, event_nonce: _Optional[int] = ..., block_height: _Optional[int] = ..., valset_nonce: _Optional[int] = ..., members: _Optional[_Iterable[_Union[_types_pb2.BridgeValidator, _Mapping]]] = ..., orchestrator: _Optional[str] = ...) -> None: ...

class MsgValsetUpdatedClaimResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgSetOrchestratorAddress(_message.Message):
    __slots__ = ["validator", "orchestrator", "eth_address"]
    VALIDATOR_FIELD_NUMBER: _ClassVar[int]
    ORCHESTRATOR_FIELD_NUMBER: _ClassVar[int]
    ETH_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    validator: str
    orchestrator: str
    eth_address: str
    def __init__(self, validator: _Optional[str] = ..., orchestrator: _Optional[str] = ..., eth_address: _Optional[str] = ...) -> None: ...

class MsgSetOrchestratorAddressResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgFxOriginatedTokenClaim(_message.Message):
    __slots__ = ["event_nonce", "block_height", "token_contract", "name", "symbol", "decimals", "orchestrator"]
    EVENT_NONCE_FIELD_NUMBER: _ClassVar[int]
    BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    DECIMALS_FIELD_NUMBER: _ClassVar[int]
    ORCHESTRATOR_FIELD_NUMBER: _ClassVar[int]
    event_nonce: int
    block_height: int
    token_contract: str
    name: str
    symbol: str
    decimals: int
    orchestrator: str
    def __init__(self, event_nonce: _Optional[int] = ..., block_height: _Optional[int] = ..., token_contract: _Optional[str] = ..., name: _Optional[str] = ..., symbol: _Optional[str] = ..., decimals: _Optional[int] = ..., orchestrator: _Optional[str] = ...) -> None: ...

class MsgFxOriginatedTokenClaimResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
