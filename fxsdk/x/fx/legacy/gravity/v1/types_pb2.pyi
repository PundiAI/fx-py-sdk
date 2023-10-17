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
    CLAIM_TYPE_DEPOSIT: _ClassVar[ClaimType]
    CLAIM_TYPE_WITHDRAW: _ClassVar[ClaimType]
    CLAIM_TYPE_ORIGINATED_TOKEN: _ClassVar[ClaimType]
    CLAIM_TYPE_VALSET_UPDATED: _ClassVar[ClaimType]
CLAIM_TYPE_UNSPECIFIED: ClaimType
CLAIM_TYPE_DEPOSIT: ClaimType
CLAIM_TYPE_WITHDRAW: ClaimType
CLAIM_TYPE_ORIGINATED_TOKEN: ClaimType
CLAIM_TYPE_VALSET_UPDATED: ClaimType

class BridgeValidator(_message.Message):
    __slots__ = ["power", "eth_address"]
    POWER_FIELD_NUMBER: _ClassVar[int]
    ETH_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    power: int
    eth_address: str
    def __init__(self, power: _Optional[int] = ..., eth_address: _Optional[str] = ...) -> None: ...

class Valset(_message.Message):
    __slots__ = ["nonce", "members", "height"]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    nonce: int
    members: _containers.RepeatedCompositeFieldContainer[BridgeValidator]
    height: int
    def __init__(self, nonce: _Optional[int] = ..., members: _Optional[_Iterable[_Union[BridgeValidator, _Mapping]]] = ..., height: _Optional[int] = ...) -> None: ...

class LastObservedEthereumBlockHeight(_message.Message):
    __slots__ = ["fx_block_height", "eth_block_height"]
    FX_BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ETH_BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    fx_block_height: int
    eth_block_height: int
    def __init__(self, fx_block_height: _Optional[int] = ..., eth_block_height: _Optional[int] = ...) -> None: ...

class ERC20ToDenom(_message.Message):
    __slots__ = ["erc20", "denom"]
    ERC20_FIELD_NUMBER: _ClassVar[int]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    erc20: str
    denom: str
    def __init__(self, erc20: _Optional[str] = ..., denom: _Optional[str] = ...) -> None: ...

class ERC20Token(_message.Message):
    __slots__ = ["contract", "amount"]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    contract: str
    amount: str
    def __init__(self, contract: _Optional[str] = ..., amount: _Optional[str] = ...) -> None: ...

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
    __slots__ = ["id", "sender", "dest_address", "erc20_token", "erc20_fee"]
    ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    DEST_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ERC20_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ERC20_FEE_FIELD_NUMBER: _ClassVar[int]
    id: int
    sender: str
    dest_address: str
    erc20_token: ERC20Token
    erc20_fee: ERC20Token
    def __init__(self, id: _Optional[int] = ..., sender: _Optional[str] = ..., dest_address: _Optional[str] = ..., erc20_token: _Optional[_Union[ERC20Token, _Mapping]] = ..., erc20_fee: _Optional[_Union[ERC20Token, _Mapping]] = ...) -> None: ...

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
