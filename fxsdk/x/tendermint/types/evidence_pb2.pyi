from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from tendermint.types import types_pb2 as _types_pb2
from tendermint.types import validator_pb2 as _validator_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Evidence(_message.Message):
    __slots__ = ["duplicate_vote_evidence", "light_client_attack_evidence"]
    DUPLICATE_VOTE_EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    LIGHT_CLIENT_ATTACK_EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    duplicate_vote_evidence: DuplicateVoteEvidence
    light_client_attack_evidence: LightClientAttackEvidence
    def __init__(self, duplicate_vote_evidence: _Optional[_Union[DuplicateVoteEvidence, _Mapping]] = ..., light_client_attack_evidence: _Optional[_Union[LightClientAttackEvidence, _Mapping]] = ...) -> None: ...

class DuplicateVoteEvidence(_message.Message):
    __slots__ = ["vote_a", "vote_b", "total_voting_power", "validator_power", "timestamp"]
    VOTE_A_FIELD_NUMBER: _ClassVar[int]
    VOTE_B_FIELD_NUMBER: _ClassVar[int]
    TOTAL_VOTING_POWER_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_POWER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    vote_a: _types_pb2.Vote
    vote_b: _types_pb2.Vote
    total_voting_power: int
    validator_power: int
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, vote_a: _Optional[_Union[_types_pb2.Vote, _Mapping]] = ..., vote_b: _Optional[_Union[_types_pb2.Vote, _Mapping]] = ..., total_voting_power: _Optional[int] = ..., validator_power: _Optional[int] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class LightClientAttackEvidence(_message.Message):
    __slots__ = ["conflicting_block", "common_height", "byzantine_validators", "total_voting_power", "timestamp"]
    CONFLICTING_BLOCK_FIELD_NUMBER: _ClassVar[int]
    COMMON_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    BYZANTINE_VALIDATORS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_VOTING_POWER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    conflicting_block: _types_pb2.LightBlock
    common_height: int
    byzantine_validators: _containers.RepeatedCompositeFieldContainer[_validator_pb2.Validator]
    total_voting_power: int
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, conflicting_block: _Optional[_Union[_types_pb2.LightBlock, _Mapping]] = ..., common_height: _Optional[int] = ..., byzantine_validators: _Optional[_Iterable[_Union[_validator_pb2.Validator, _Mapping]]] = ..., total_voting_power: _Optional[int] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EvidenceList(_message.Message):
    __slots__ = ["evidence"]
    EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    evidence: _containers.RepeatedCompositeFieldContainer[Evidence]
    def __init__(self, evidence: _Optional[_Iterable[_Union[Evidence, _Mapping]]] = ...) -> None: ...
