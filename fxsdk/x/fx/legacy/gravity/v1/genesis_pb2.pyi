from fxpysdk.fxsdk.x.fx.legacy.gravity.v1 import tx_pb2 as _tx_pb2
from fxpysdk.fxsdk.x.fx.legacy.gravity.v1 import types_pb2 as _types_pb2
from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Params(_message.Message):
    __slots__ = ["gravity_id", "contract_source_hash", "bridge_eth_address", "bridge_chain_id", "signed_valsets_window", "signed_batches_window", "signed_claims_window", "target_batch_timeout", "average_block_time", "average_eth_block_time", "slash_fraction_valset", "slash_fraction_batch", "slash_fraction_claim", "slash_fraction_conflicting_claim", "unbond_slashing_valsets_window", "ibc_transfer_timeout_height", "valset_update_power_change_percent"]
    GRAVITY_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_SOURCE_HASH_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_ETH_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNED_VALSETS_WINDOW_FIELD_NUMBER: _ClassVar[int]
    SIGNED_BATCHES_WINDOW_FIELD_NUMBER: _ClassVar[int]
    SIGNED_CLAIMS_WINDOW_FIELD_NUMBER: _ClassVar[int]
    TARGET_BATCH_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_BLOCK_TIME_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_ETH_BLOCK_TIME_FIELD_NUMBER: _ClassVar[int]
    SLASH_FRACTION_VALSET_FIELD_NUMBER: _ClassVar[int]
    SLASH_FRACTION_BATCH_FIELD_NUMBER: _ClassVar[int]
    SLASH_FRACTION_CLAIM_FIELD_NUMBER: _ClassVar[int]
    SLASH_FRACTION_CONFLICTING_CLAIM_FIELD_NUMBER: _ClassVar[int]
    UNBOND_SLASHING_VALSETS_WINDOW_FIELD_NUMBER: _ClassVar[int]
    IBC_TRANSFER_TIMEOUT_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    VALSET_UPDATE_POWER_CHANGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    gravity_id: str
    contract_source_hash: str
    bridge_eth_address: str
    bridge_chain_id: int
    signed_valsets_window: int
    signed_batches_window: int
    signed_claims_window: int
    target_batch_timeout: int
    average_block_time: int
    average_eth_block_time: int
    slash_fraction_valset: bytes
    slash_fraction_batch: bytes
    slash_fraction_claim: bytes
    slash_fraction_conflicting_claim: bytes
    unbond_slashing_valsets_window: int
    ibc_transfer_timeout_height: int
    valset_update_power_change_percent: bytes
    def __init__(self, gravity_id: _Optional[str] = ..., contract_source_hash: _Optional[str] = ..., bridge_eth_address: _Optional[str] = ..., bridge_chain_id: _Optional[int] = ..., signed_valsets_window: _Optional[int] = ..., signed_batches_window: _Optional[int] = ..., signed_claims_window: _Optional[int] = ..., target_batch_timeout: _Optional[int] = ..., average_block_time: _Optional[int] = ..., average_eth_block_time: _Optional[int] = ..., slash_fraction_valset: _Optional[bytes] = ..., slash_fraction_batch: _Optional[bytes] = ..., slash_fraction_claim: _Optional[bytes] = ..., slash_fraction_conflicting_claim: _Optional[bytes] = ..., unbond_slashing_valsets_window: _Optional[int] = ..., ibc_transfer_timeout_height: _Optional[int] = ..., valset_update_power_change_percent: _Optional[bytes] = ...) -> None: ...

class GenesisState(_message.Message):
    __slots__ = ["params", "last_observed_nonce", "last_observed_block_height", "delegate_keys", "valsets", "erc20_to_denoms", "unbatched_transfers", "batches", "batch_confirms", "valset_confirms", "attestations", "last_observed_valset", "last_slashed_batch_block", "last_slashed_valset_nonce", "last_tx_pool_id", "last_batch_id"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    LAST_OBSERVED_NONCE_FIELD_NUMBER: _ClassVar[int]
    LAST_OBSERVED_BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    DELEGATE_KEYS_FIELD_NUMBER: _ClassVar[int]
    VALSETS_FIELD_NUMBER: _ClassVar[int]
    ERC20_TO_DENOMS_FIELD_NUMBER: _ClassVar[int]
    UNBATCHED_TRANSFERS_FIELD_NUMBER: _ClassVar[int]
    BATCHES_FIELD_NUMBER: _ClassVar[int]
    BATCH_CONFIRMS_FIELD_NUMBER: _ClassVar[int]
    VALSET_CONFIRMS_FIELD_NUMBER: _ClassVar[int]
    ATTESTATIONS_FIELD_NUMBER: _ClassVar[int]
    LAST_OBSERVED_VALSET_FIELD_NUMBER: _ClassVar[int]
    LAST_SLASHED_BATCH_BLOCK_FIELD_NUMBER: _ClassVar[int]
    LAST_SLASHED_VALSET_NONCE_FIELD_NUMBER: _ClassVar[int]
    LAST_TX_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    params: Params
    last_observed_nonce: int
    last_observed_block_height: _types_pb2.LastObservedEthereumBlockHeight
    delegate_keys: _containers.RepeatedCompositeFieldContainer[_tx_pb2.MsgSetOrchestratorAddress]
    valsets: _containers.RepeatedCompositeFieldContainer[_types_pb2.Valset]
    erc20_to_denoms: _containers.RepeatedCompositeFieldContainer[_types_pb2.ERC20ToDenom]
    unbatched_transfers: _containers.RepeatedCompositeFieldContainer[_types_pb2.OutgoingTransferTx]
    batches: _containers.RepeatedCompositeFieldContainer[_types_pb2.OutgoingTxBatch]
    batch_confirms: _containers.RepeatedCompositeFieldContainer[_tx_pb2.MsgConfirmBatch]
    valset_confirms: _containers.RepeatedCompositeFieldContainer[_tx_pb2.MsgValsetConfirm]
    attestations: _containers.RepeatedCompositeFieldContainer[_types_pb2.Attestation]
    last_observed_valset: _types_pb2.Valset
    last_slashed_batch_block: int
    last_slashed_valset_nonce: int
    last_tx_pool_id: int
    last_batch_id: int
    def __init__(self, params: _Optional[_Union[Params, _Mapping]] = ..., last_observed_nonce: _Optional[int] = ..., last_observed_block_height: _Optional[_Union[_types_pb2.LastObservedEthereumBlockHeight, _Mapping]] = ..., delegate_keys: _Optional[_Iterable[_Union[_tx_pb2.MsgSetOrchestratorAddress, _Mapping]]] = ..., valsets: _Optional[_Iterable[_Union[_types_pb2.Valset, _Mapping]]] = ..., erc20_to_denoms: _Optional[_Iterable[_Union[_types_pb2.ERC20ToDenom, _Mapping]]] = ..., unbatched_transfers: _Optional[_Iterable[_Union[_types_pb2.OutgoingTransferTx, _Mapping]]] = ..., batches: _Optional[_Iterable[_Union[_types_pb2.OutgoingTxBatch, _Mapping]]] = ..., batch_confirms: _Optional[_Iterable[_Union[_tx_pb2.MsgConfirmBatch, _Mapping]]] = ..., valset_confirms: _Optional[_Iterable[_Union[_tx_pb2.MsgValsetConfirm, _Mapping]]] = ..., attestations: _Optional[_Iterable[_Union[_types_pb2.Attestation, _Mapping]]] = ..., last_observed_valset: _Optional[_Union[_types_pb2.Valset, _Mapping]] = ..., last_slashed_batch_block: _Optional[int] = ..., last_slashed_valset_nonce: _Optional[int] = ..., last_tx_pool_id: _Optional[int] = ..., last_batch_id: _Optional[int] = ...) -> None: ...
