from fxsdk.x.fx.crosschain.v1 import tx_pb2 as _tx_pb2
from fxsdk.x.fx.crosschain.v1 import types_pb2 as _types_pb2
from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ["params", "last_observed_event_nonce", "last_observed_block_height", "oracles", "oracle_sets", "bridge_tokens", "unbatched_transfers", "batches", "oracle_set_confirms", "batch_confirms", "attestations", "proposal_oracle", "last_observed_oracle_set", "last_slashed_batch_block", "last_slashed_oracle_set_nonce"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    LAST_OBSERVED_EVENT_NONCE_FIELD_NUMBER: _ClassVar[int]
    LAST_OBSERVED_BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ORACLES_FIELD_NUMBER: _ClassVar[int]
    ORACLE_SETS_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_TOKENS_FIELD_NUMBER: _ClassVar[int]
    UNBATCHED_TRANSFERS_FIELD_NUMBER: _ClassVar[int]
    BATCHES_FIELD_NUMBER: _ClassVar[int]
    ORACLE_SET_CONFIRMS_FIELD_NUMBER: _ClassVar[int]
    BATCH_CONFIRMS_FIELD_NUMBER: _ClassVar[int]
    ATTESTATIONS_FIELD_NUMBER: _ClassVar[int]
    PROPOSAL_ORACLE_FIELD_NUMBER: _ClassVar[int]
    LAST_OBSERVED_ORACLE_SET_FIELD_NUMBER: _ClassVar[int]
    LAST_SLASHED_BATCH_BLOCK_FIELD_NUMBER: _ClassVar[int]
    LAST_SLASHED_ORACLE_SET_NONCE_FIELD_NUMBER: _ClassVar[int]
    params: _types_pb2.Params
    last_observed_event_nonce: int
    last_observed_block_height: _types_pb2.LastObservedBlockHeight
    oracles: _containers.RepeatedCompositeFieldContainer[_types_pb2.Oracle]
    oracle_sets: _containers.RepeatedCompositeFieldContainer[_types_pb2.OracleSet]
    bridge_tokens: _containers.RepeatedCompositeFieldContainer[_types_pb2.BridgeToken]
    unbatched_transfers: _containers.RepeatedCompositeFieldContainer[_types_pb2.OutgoingTransferTx]
    batches: _containers.RepeatedCompositeFieldContainer[_types_pb2.OutgoingTxBatch]
    oracle_set_confirms: _containers.RepeatedCompositeFieldContainer[_tx_pb2.MsgOracleSetConfirm]
    batch_confirms: _containers.RepeatedCompositeFieldContainer[_tx_pb2.MsgConfirmBatch]
    attestations: _containers.RepeatedCompositeFieldContainer[_types_pb2.Attestation]
    proposal_oracle: _types_pb2.ProposalOracle
    last_observed_oracle_set: _types_pb2.OracleSet
    last_slashed_batch_block: int
    last_slashed_oracle_set_nonce: int
    def __init__(self, params: _Optional[_Union[_types_pb2.Params, _Mapping]] = ..., last_observed_event_nonce: _Optional[int] = ..., last_observed_block_height: _Optional[_Union[_types_pb2.LastObservedBlockHeight, _Mapping]] = ..., oracles: _Optional[_Iterable[_Union[_types_pb2.Oracle, _Mapping]]] = ..., oracle_sets: _Optional[_Iterable[_Union[_types_pb2.OracleSet, _Mapping]]] = ..., bridge_tokens: _Optional[_Iterable[_Union[_types_pb2.BridgeToken, _Mapping]]] = ..., unbatched_transfers: _Optional[_Iterable[_Union[_types_pb2.OutgoingTransferTx, _Mapping]]] = ..., batches: _Optional[_Iterable[_Union[_types_pb2.OutgoingTxBatch, _Mapping]]] = ..., oracle_set_confirms: _Optional[_Iterable[_Union[_tx_pb2.MsgOracleSetConfirm, _Mapping]]] = ..., batch_confirms: _Optional[_Iterable[_Union[_tx_pb2.MsgConfirmBatch, _Mapping]]] = ..., attestations: _Optional[_Iterable[_Union[_types_pb2.Attestation, _Mapping]]] = ..., proposal_oracle: _Optional[_Union[_types_pb2.ProposalOracle, _Mapping]] = ..., last_observed_oracle_set: _Optional[_Union[_types_pb2.OracleSet, _Mapping]] = ..., last_slashed_batch_block: _Optional[int] = ..., last_slashed_oracle_set_nonce: _Optional[int] = ...) -> None: ...
