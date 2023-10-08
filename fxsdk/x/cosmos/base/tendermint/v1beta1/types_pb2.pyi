from gogoproto import gogo_pb2 as _gogo_pb2
from tendermint.types import types_pb2 as _types_pb2
from tendermint.types import evidence_pb2 as _evidence_pb2
from tendermint.version import types_pb2 as _types_pb2_1
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Block(_message.Message):
    __slots__ = ["header", "data", "evidence", "last_commit"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    LAST_COMMIT_FIELD_NUMBER: _ClassVar[int]
    header: Header
    data: _types_pb2.Data
    evidence: _evidence_pb2.EvidenceList
    last_commit: _types_pb2.Commit
    def __init__(self, header: _Optional[_Union[Header, _Mapping]] = ..., data: _Optional[_Union[_types_pb2.Data, _Mapping]] = ..., evidence: _Optional[_Union[_evidence_pb2.EvidenceList, _Mapping]] = ..., last_commit: _Optional[_Union[_types_pb2.Commit, _Mapping]] = ...) -> None: ...

class Header(_message.Message):
    __slots__ = ["version", "chain_id", "height", "time", "last_block_id", "last_commit_hash", "data_hash", "validators_hash", "next_validators_hash", "consensus_hash", "app_hash", "last_results_hash", "evidence_hash", "proposer_address"]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_COMMIT_HASH_FIELD_NUMBER: _ClassVar[int]
    DATA_HASH_FIELD_NUMBER: _ClassVar[int]
    VALIDATORS_HASH_FIELD_NUMBER: _ClassVar[int]
    NEXT_VALIDATORS_HASH_FIELD_NUMBER: _ClassVar[int]
    CONSENSUS_HASH_FIELD_NUMBER: _ClassVar[int]
    APP_HASH_FIELD_NUMBER: _ClassVar[int]
    LAST_RESULTS_HASH_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_HASH_FIELD_NUMBER: _ClassVar[int]
    PROPOSER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    version: _types_pb2_1.Consensus
    chain_id: str
    height: int
    time: _timestamp_pb2.Timestamp
    last_block_id: _types_pb2.BlockID
    last_commit_hash: bytes
    data_hash: bytes
    validators_hash: bytes
    next_validators_hash: bytes
    consensus_hash: bytes
    app_hash: bytes
    last_results_hash: bytes
    evidence_hash: bytes
    proposer_address: str
    def __init__(self, version: _Optional[_Union[_types_pb2_1.Consensus, _Mapping]] = ..., chain_id: _Optional[str] = ..., height: _Optional[int] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_block_id: _Optional[_Union[_types_pb2.BlockID, _Mapping]] = ..., last_commit_hash: _Optional[bytes] = ..., data_hash: _Optional[bytes] = ..., validators_hash: _Optional[bytes] = ..., next_validators_hash: _Optional[bytes] = ..., consensus_hash: _Optional[bytes] = ..., app_hash: _Optional[bytes] = ..., last_results_hash: _Optional[bytes] = ..., evidence_hash: _Optional[bytes] = ..., proposer_address: _Optional[str] = ...) -> None: ...
