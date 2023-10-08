from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from cosmos.msg.v1 import msg_pb2 as _msg_pb2
from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from fx.crosschain.v1 import types_pb2 as _types_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MsgBondedOracle(_message.Message):
    __slots__ = ["chain_name", "oracle_address", "bridger_address", "external_address", "validator_address", "delegate_amount"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    ORACLE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BRIDGER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DELEGATE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    oracle_address: str
    bridger_address: str
    external_address: str
    validator_address: str
    delegate_amount: _coin_pb2.Coin
    def __init__(self, chain_name: _Optional[str] = ..., oracle_address: _Optional[str] = ..., bridger_address: _Optional[str] = ..., external_address: _Optional[str] = ..., validator_address: _Optional[str] = ..., delegate_amount: _Optional[_Union[_coin_pb2.Coin, _Mapping]] = ...) -> None: ...

class MsgBondedOracleResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgAddDelegate(_message.Message):
    __slots__ = ["chain_name", "oracle_address", "amount"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    ORACLE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    oracle_address: str
    amount: _coin_pb2.Coin
    def __init__(self, chain_name: _Optional[str] = ..., oracle_address: _Optional[str] = ..., amount: _Optional[_Union[_coin_pb2.Coin, _Mapping]] = ...) -> None: ...

class MsgAddDelegateResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgReDelegate(_message.Message):
    __slots__ = ["chain_name", "oracle_address", "validator_address"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    ORACLE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    oracle_address: str
    validator_address: str
    def __init__(self, chain_name: _Optional[str] = ..., oracle_address: _Optional[str] = ..., validator_address: _Optional[str] = ...) -> None: ...

class MsgReDelegateResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgEditBridger(_message.Message):
    __slots__ = ["chain_name", "oracle_address", "bridger_address"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    ORACLE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BRIDGER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    oracle_address: str
    bridger_address: str
    def __init__(self, chain_name: _Optional[str] = ..., oracle_address: _Optional[str] = ..., bridger_address: _Optional[str] = ...) -> None: ...

class MsgEditBridgerResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgUnbondedOracle(_message.Message):
    __slots__ = ["chain_name", "oracle_address"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    ORACLE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    oracle_address: str
    def __init__(self, chain_name: _Optional[str] = ..., oracle_address: _Optional[str] = ...) -> None: ...

class MsgUnbondedOracleResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgWithdrawReward(_message.Message):
    __slots__ = ["chain_name", "oracle_address"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    ORACLE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    oracle_address: str
    def __init__(self, chain_name: _Optional[str] = ..., oracle_address: _Optional[str] = ...) -> None: ...

class MsgWithdrawRewardResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgOracleSetConfirm(_message.Message):
    __slots__ = ["nonce", "bridger_address", "external_address", "signature", "chain_name"]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    BRIDGER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    nonce: int
    bridger_address: str
    external_address: str
    signature: str
    chain_name: str
    def __init__(self, nonce: _Optional[int] = ..., bridger_address: _Optional[str] = ..., external_address: _Optional[str] = ..., signature: _Optional[str] = ..., chain_name: _Optional[str] = ...) -> None: ...

class MsgOracleSetConfirmResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgOracleSetUpdatedClaim(_message.Message):
    __slots__ = ["event_nonce", "block_height", "oracle_set_nonce", "members", "bridger_address", "chain_name"]
    EVENT_NONCE_FIELD_NUMBER: _ClassVar[int]
    BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ORACLE_SET_NONCE_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    BRIDGER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    event_nonce: int
    block_height: int
    oracle_set_nonce: int
    members: _containers.RepeatedCompositeFieldContainer[_types_pb2.BridgeValidator]
    bridger_address: str
    chain_name: str
    def __init__(self, event_nonce: _Optional[int] = ..., block_height: _Optional[int] = ..., oracle_set_nonce: _Optional[int] = ..., members: _Optional[_Iterable[_Union[_types_pb2.BridgeValidator, _Mapping]]] = ..., bridger_address: _Optional[str] = ..., chain_name: _Optional[str] = ...) -> None: ...

class MsgOracleSetUpdatedClaimResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgSendToFxClaim(_message.Message):
    __slots__ = ["event_nonce", "block_height", "token_contract", "amount", "sender", "receiver", "target_ibc", "bridger_address", "chain_name"]
    EVENT_NONCE_FIELD_NUMBER: _ClassVar[int]
    BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_FIELD_NUMBER: _ClassVar[int]
    TARGET_IBC_FIELD_NUMBER: _ClassVar[int]
    BRIDGER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    event_nonce: int
    block_height: int
    token_contract: str
    amount: str
    sender: str
    receiver: str
    target_ibc: str
    bridger_address: str
    chain_name: str
    def __init__(self, event_nonce: _Optional[int] = ..., block_height: _Optional[int] = ..., token_contract: _Optional[str] = ..., amount: _Optional[str] = ..., sender: _Optional[str] = ..., receiver: _Optional[str] = ..., target_ibc: _Optional[str] = ..., bridger_address: _Optional[str] = ..., chain_name: _Optional[str] = ...) -> None: ...

class MsgSendToFxClaimResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgSendToExternal(_message.Message):
    __slots__ = ["sender", "dest", "amount", "bridge_fee", "chain_name"]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    DEST_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_FEE_FIELD_NUMBER: _ClassVar[int]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    sender: str
    dest: str
    amount: _coin_pb2.Coin
    bridge_fee: _coin_pb2.Coin
    chain_name: str
    def __init__(self, sender: _Optional[str] = ..., dest: _Optional[str] = ..., amount: _Optional[_Union[_coin_pb2.Coin, _Mapping]] = ..., bridge_fee: _Optional[_Union[_coin_pb2.Coin, _Mapping]] = ..., chain_name: _Optional[str] = ...) -> None: ...

class MsgSendToExternalResponse(_message.Message):
    __slots__ = ["outgoing_tx_id"]
    OUTGOING_TX_ID_FIELD_NUMBER: _ClassVar[int]
    outgoing_tx_id: int
    def __init__(self, outgoing_tx_id: _Optional[int] = ...) -> None: ...

class MsgCancelSendToExternal(_message.Message):
    __slots__ = ["transaction_id", "sender", "chain_name"]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    transaction_id: int
    sender: str
    chain_name: str
    def __init__(self, transaction_id: _Optional[int] = ..., sender: _Optional[str] = ..., chain_name: _Optional[str] = ...) -> None: ...

class MsgCancelSendToExternalResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgRequestBatch(_message.Message):
    __slots__ = ["sender", "denom", "minimum_fee", "fee_receive", "chain_name", "base_fee"]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_FEE_FIELD_NUMBER: _ClassVar[int]
    FEE_RECEIVE_FIELD_NUMBER: _ClassVar[int]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    BASE_FEE_FIELD_NUMBER: _ClassVar[int]
    sender: str
    denom: str
    minimum_fee: str
    fee_receive: str
    chain_name: str
    base_fee: str
    def __init__(self, sender: _Optional[str] = ..., denom: _Optional[str] = ..., minimum_fee: _Optional[str] = ..., fee_receive: _Optional[str] = ..., chain_name: _Optional[str] = ..., base_fee: _Optional[str] = ...) -> None: ...

class MsgRequestBatchResponse(_message.Message):
    __slots__ = ["batch_nonce"]
    BATCH_NONCE_FIELD_NUMBER: _ClassVar[int]
    batch_nonce: int
    def __init__(self, batch_nonce: _Optional[int] = ...) -> None: ...

class MsgConfirmBatch(_message.Message):
    __slots__ = ["nonce", "token_contract", "bridger_address", "external_address", "signature", "chain_name"]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    BRIDGER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    nonce: int
    token_contract: str
    bridger_address: str
    external_address: str
    signature: str
    chain_name: str
    def __init__(self, nonce: _Optional[int] = ..., token_contract: _Optional[str] = ..., bridger_address: _Optional[str] = ..., external_address: _Optional[str] = ..., signature: _Optional[str] = ..., chain_name: _Optional[str] = ...) -> None: ...

class MsgConfirmBatchResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgSendToExternalClaim(_message.Message):
    __slots__ = ["event_nonce", "block_height", "batch_nonce", "token_contract", "bridger_address", "chain_name"]
    EVENT_NONCE_FIELD_NUMBER: _ClassVar[int]
    BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    BATCH_NONCE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    BRIDGER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    event_nonce: int
    block_height: int
    batch_nonce: int
    token_contract: str
    bridger_address: str
    chain_name: str
    def __init__(self, event_nonce: _Optional[int] = ..., block_height: _Optional[int] = ..., batch_nonce: _Optional[int] = ..., token_contract: _Optional[str] = ..., bridger_address: _Optional[str] = ..., chain_name: _Optional[str] = ...) -> None: ...

class MsgSendToExternalClaimResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgBridgeTokenClaim(_message.Message):
    __slots__ = ["event_nonce", "block_height", "token_contract", "name", "symbol", "decimals", "bridger_address", "channel_ibc", "chain_name"]
    EVENT_NONCE_FIELD_NUMBER: _ClassVar[int]
    BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    DECIMALS_FIELD_NUMBER: _ClassVar[int]
    BRIDGER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_IBC_FIELD_NUMBER: _ClassVar[int]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    event_nonce: int
    block_height: int
    token_contract: str
    name: str
    symbol: str
    decimals: int
    bridger_address: str
    channel_ibc: str
    chain_name: str
    def __init__(self, event_nonce: _Optional[int] = ..., block_height: _Optional[int] = ..., token_contract: _Optional[str] = ..., name: _Optional[str] = ..., symbol: _Optional[str] = ..., decimals: _Optional[int] = ..., bridger_address: _Optional[str] = ..., channel_ibc: _Optional[str] = ..., chain_name: _Optional[str] = ...) -> None: ...

class MsgBridgeTokenClaimResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgSetOrchestratorAddress(_message.Message):
    __slots__ = ["oracle_address", "bridger_address", "external_address", "deposit", "chain_name"]
    ORACLE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BRIDGER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DEPOSIT_FIELD_NUMBER: _ClassVar[int]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    oracle_address: str
    bridger_address: str
    external_address: str
    deposit: _coin_pb2.Coin
    chain_name: str
    def __init__(self, oracle_address: _Optional[str] = ..., bridger_address: _Optional[str] = ..., external_address: _Optional[str] = ..., deposit: _Optional[_Union[_coin_pb2.Coin, _Mapping]] = ..., chain_name: _Optional[str] = ...) -> None: ...

class MsgAddOracleDeposit(_message.Message):
    __slots__ = ["oracle_address", "amount", "chain_name"]
    ORACLE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    oracle_address: str
    amount: _coin_pb2.Coin
    chain_name: str
    def __init__(self, oracle_address: _Optional[str] = ..., amount: _Optional[_Union[_coin_pb2.Coin, _Mapping]] = ..., chain_name: _Optional[str] = ...) -> None: ...

class MsgUpdateParams(_message.Message):
    __slots__ = ["chain_name", "authority", "params"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    authority: str
    params: _types_pb2.Params
    def __init__(self, chain_name: _Optional[str] = ..., authority: _Optional[str] = ..., params: _Optional[_Union[_types_pb2.Params, _Mapping]] = ...) -> None: ...

class MsgUpdateParamsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgIncreaseBridgeFee(_message.Message):
    __slots__ = ["chain_name", "transaction_id", "sender", "add_bridge_fee"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    ADD_BRIDGE_FEE_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    transaction_id: int
    sender: str
    add_bridge_fee: _coin_pb2.Coin
    def __init__(self, chain_name: _Optional[str] = ..., transaction_id: _Optional[int] = ..., sender: _Optional[str] = ..., add_bridge_fee: _Optional[_Union[_coin_pb2.Coin, _Mapping]] = ...) -> None: ...

class MsgIncreaseBridgeFeeResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgUpdateChainOracles(_message.Message):
    __slots__ = ["chain_name", "authority", "oracles"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    ORACLES_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    authority: str
    oracles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, chain_name: _Optional[str] = ..., authority: _Optional[str] = ..., oracles: _Optional[_Iterable[str]] = ...) -> None: ...

class MsgUpdateChainOraclesResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
