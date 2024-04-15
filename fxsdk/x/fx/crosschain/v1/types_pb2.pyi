from fxsdk.x.cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClaimType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CLAIM_TYPE_UNSPECIFIED: _ClassVar[ClaimType]
    CLAIM_TYPE_SEND_TO_FX: _ClassVar[ClaimType]
    CLAIM_TYPE_SEND_TO_EXTERNAL: _ClassVar[ClaimType]
    CLAIM_TYPE_BRIDGE_TOKEN: _ClassVar[ClaimType]
    CLAIM_TYPE_ORACLE_SET_UPDATED: _ClassVar[ClaimType]
CLAIM_TYPE_UNSPECIFIED: ClaimType
CLAIM_TYPE_SEND_TO_FX: ClaimType
CLAIM_TYPE_SEND_TO_EXTERNAL: ClaimType
CLAIM_TYPE_BRIDGE_TOKEN: ClaimType
CLAIM_TYPE_ORACLE_SET_UPDATED: ClaimType

class ProposalOracle(_message.Message):
    __slots__ = ["oracles"]
    ORACLES_FIELD_NUMBER: _ClassVar[int]
    oracles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, oracles: _Optional[_Iterable[str]] = ...) -> None: ...

class Oracle(_message.Message):
    __slots__ = ["oracle_address", "bridger_address", "external_address", "delegate_amount", "start_height", "online", "delegate_validator", "slash_times"]
    ORACLE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BRIDGER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DELEGATE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    START_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    DELEGATE_VALIDATOR_FIELD_NUMBER: _ClassVar[int]
    SLASH_TIMES_FIELD_NUMBER: _ClassVar[int]
    oracle_address: str
    bridger_address: str
    external_address: str
    delegate_amount: str
    start_height: int
    online: bool
    delegate_validator: str
    slash_times: int
    def __init__(self, oracle_address: _Optional[str] = ..., bridger_address: _Optional[str] = ..., external_address: _Optional[str] = ..., delegate_amount: _Optional[str] = ..., start_height: _Optional[int] = ..., online: bool = ..., delegate_validator: _Optional[str] = ..., slash_times: _Optional[int] = ...) -> None: ...

class BridgeValidator(_message.Message):
    __slots__ = ["power", "external_address"]
    POWER_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    power: int
    external_address: str
    def __init__(self, power: _Optional[int] = ..., external_address: _Optional[str] = ...) -> None: ...

class OracleSet(_message.Message):
    __slots__ = ["nonce", "members", "height"]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    nonce: int
    members: _containers.RepeatedCompositeFieldContainer[BridgeValidator]
    height: int
    def __init__(self, nonce: _Optional[int] = ..., members: _Optional[_Iterable[_Union[BridgeValidator, _Mapping]]] = ..., height: _Optional[int] = ...) -> None: ...

class LastObservedBlockHeight(_message.Message):
    __slots__ = ["external_block_height", "block_height"]
    EXTERNAL_BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    external_block_height: int
    block_height: int
    def __init__(self, external_block_height: _Optional[int] = ..., block_height: _Optional[int] = ...) -> None: ...

class BridgeToken(_message.Message):
    __slots__ = ["token", "denom", "channel_ibc"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_IBC_FIELD_NUMBER: _ClassVar[int]
    token: str
    denom: str
    channel_ibc: str
    def __init__(self, token: _Optional[str] = ..., denom: _Optional[str] = ..., channel_ibc: _Optional[str] = ...) -> None: ...

class Attestation(_message.Message):
    __slots__ = ["observed", "votes", "height", "claim"]
    OBSERVED_FIELD_NUMBER: _ClassVar[int]
    VOTES_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    CLAIM_FIELD_NUMBER: _ClassVar[int]
    observed: bool
    votes: _containers.RepeatedScalarFieldContainer[str]
    height: int
    claim: _any_pb2.Any
    def __init__(self, observed: bool = ..., votes: _Optional[_Iterable[str]] = ..., height: _Optional[int] = ..., claim: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class OutgoingTxBatch(_message.Message):
    __slots__ = ["batch_nonce", "batch_timeout", "transactions", "token_contract", "block", "feeReceive"]
    BATCH_NONCE_FIELD_NUMBER: _ClassVar[int]
    BATCH_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    FEERECEIVE_FIELD_NUMBER: _ClassVar[int]
    batch_nonce: int
    batch_timeout: int
    transactions: _containers.RepeatedCompositeFieldContainer[OutgoingTransferTx]
    token_contract: str
    block: int
    feeReceive: str
    def __init__(self, batch_nonce: _Optional[int] = ..., batch_timeout: _Optional[int] = ..., transactions: _Optional[_Iterable[_Union[OutgoingTransferTx, _Mapping]]] = ..., token_contract: _Optional[str] = ..., block: _Optional[int] = ..., feeReceive: _Optional[str] = ...) -> None: ...

class OutgoingTransferTx(_message.Message):
    __slots__ = ["id", "sender", "dest_address", "token", "fee"]
    ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    DEST_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    FEE_FIELD_NUMBER: _ClassVar[int]
    id: int
    sender: str
    dest_address: str
    token: ERC20Token
    fee: ERC20Token
    def __init__(self, id: _Optional[int] = ..., sender: _Optional[str] = ..., dest_address: _Optional[str] = ..., token: _Optional[_Union[ERC20Token, _Mapping]] = ..., fee: _Optional[_Union[ERC20Token, _Mapping]] = ...) -> None: ...

class ERC20Token(_message.Message):
    __slots__ = ["contract", "amount"]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    contract: str
    amount: str
    def __init__(self, contract: _Optional[str] = ..., amount: _Optional[str] = ...) -> None: ...

class IDSet(_message.Message):
    __slots__ = ["ids"]
    IDS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, ids: _Optional[_Iterable[int]] = ...) -> None: ...

class BatchFees(_message.Message):
    __slots__ = ["token_contract", "total_fees", "total_txs", "total_amount"]
    TOKEN_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FEES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TXS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    token_contract: str
    total_fees: str
    total_txs: int
    total_amount: str
    def __init__(self, token_contract: _Optional[str] = ..., total_fees: _Optional[str] = ..., total_txs: _Optional[int] = ..., total_amount: _Optional[str] = ...) -> None: ...

class MinBatchFee(_message.Message):
    __slots__ = ["token_contract", "baseFee"]
    TOKEN_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    BASEFEE_FIELD_NUMBER: _ClassVar[int]
    token_contract: str
    baseFee: str
    def __init__(self, token_contract: _Optional[str] = ..., baseFee: _Optional[str] = ...) -> None: ...

class Params(_message.Message):
    __slots__ = ["gravity_id", "average_block_time", "external_batch_timeout", "average_external_block_time", "signed_window", "slash_fraction", "oracle_set_update_power_change_percent", "ibc_transfer_timeout_height", "oracles", "delegate_threshold", "delegate_multiple"]
    GRAVITY_ID_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_BLOCK_TIME_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_BATCH_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_EXTERNAL_BLOCK_TIME_FIELD_NUMBER: _ClassVar[int]
    SIGNED_WINDOW_FIELD_NUMBER: _ClassVar[int]
    SLASH_FRACTION_FIELD_NUMBER: _ClassVar[int]
    ORACLE_SET_UPDATE_POWER_CHANGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    IBC_TRANSFER_TIMEOUT_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ORACLES_FIELD_NUMBER: _ClassVar[int]
    DELEGATE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    DELEGATE_MULTIPLE_FIELD_NUMBER: _ClassVar[int]
    gravity_id: str
    average_block_time: int
    external_batch_timeout: int
    average_external_block_time: int
    signed_window: int
    slash_fraction: bytes
    oracle_set_update_power_change_percent: bytes
    ibc_transfer_timeout_height: int
    oracles: _containers.RepeatedScalarFieldContainer[str]
    delegate_threshold: _coin_pb2.Coin
    delegate_multiple: int
    def __init__(self, gravity_id: _Optional[str] = ..., average_block_time: _Optional[int] = ..., external_batch_timeout: _Optional[int] = ..., average_external_block_time: _Optional[int] = ..., signed_window: _Optional[int] = ..., slash_fraction: _Optional[bytes] = ..., oracle_set_update_power_change_percent: _Optional[bytes] = ..., ibc_transfer_timeout_height: _Optional[int] = ..., oracles: _Optional[_Iterable[str]] = ..., delegate_threshold: _Optional[_Union[_coin_pb2.Coin, _Mapping]] = ..., delegate_multiple: _Optional[int] = ...) -> None: ...

class InitCrossChainParamsProposal(_message.Message):
    __slots__ = ["title", "description", "params", "chain_name"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    params: Params
    chain_name: str
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., params: _Optional[_Union[Params, _Mapping]] = ..., chain_name: _Optional[str] = ...) -> None: ...

class UpdateChainOraclesProposal(_message.Message):
    __slots__ = ["title", "description", "oracles", "chain_name"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ORACLES_FIELD_NUMBER: _ClassVar[int]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    oracles: _containers.RepeatedScalarFieldContainer[str]
    chain_name: str
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., oracles: _Optional[_Iterable[str]] = ..., chain_name: _Optional[str] = ...) -> None: ...
