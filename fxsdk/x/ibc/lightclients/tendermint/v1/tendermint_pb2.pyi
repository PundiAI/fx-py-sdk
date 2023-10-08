from tendermint.types import validator_pb2 as _validator_pb2
from tendermint.types import types_pb2 as _types_pb2
import proofs_pb2 as _proofs_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ibc.core.client.v1 import client_pb2 as _client_pb2
from ibc.core.commitment.v1 import commitment_pb2 as _commitment_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClientState(_message.Message):
    __slots__ = ["chain_id", "trust_level", "trusting_period", "unbonding_period", "max_clock_drift", "frozen_height", "latest_height", "proof_specs", "upgrade_path", "allow_update_after_expiry", "allow_update_after_misbehaviour"]
    CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    TRUST_LEVEL_FIELD_NUMBER: _ClassVar[int]
    TRUSTING_PERIOD_FIELD_NUMBER: _ClassVar[int]
    UNBONDING_PERIOD_FIELD_NUMBER: _ClassVar[int]
    MAX_CLOCK_DRIFT_FIELD_NUMBER: _ClassVar[int]
    FROZEN_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    LATEST_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    PROOF_SPECS_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_PATH_FIELD_NUMBER: _ClassVar[int]
    ALLOW_UPDATE_AFTER_EXPIRY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_UPDATE_AFTER_MISBEHAVIOUR_FIELD_NUMBER: _ClassVar[int]
    chain_id: str
    trust_level: Fraction
    trusting_period: _duration_pb2.Duration
    unbonding_period: _duration_pb2.Duration
    max_clock_drift: _duration_pb2.Duration
    frozen_height: _client_pb2.Height
    latest_height: _client_pb2.Height
    proof_specs: _containers.RepeatedCompositeFieldContainer[_proofs_pb2.ProofSpec]
    upgrade_path: _containers.RepeatedScalarFieldContainer[str]
    allow_update_after_expiry: bool
    allow_update_after_misbehaviour: bool
    def __init__(self, chain_id: _Optional[str] = ..., trust_level: _Optional[_Union[Fraction, _Mapping]] = ..., trusting_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., unbonding_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., max_clock_drift: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., frozen_height: _Optional[_Union[_client_pb2.Height, _Mapping]] = ..., latest_height: _Optional[_Union[_client_pb2.Height, _Mapping]] = ..., proof_specs: _Optional[_Iterable[_Union[_proofs_pb2.ProofSpec, _Mapping]]] = ..., upgrade_path: _Optional[_Iterable[str]] = ..., allow_update_after_expiry: bool = ..., allow_update_after_misbehaviour: bool = ...) -> None: ...

class ConsensusState(_message.Message):
    __slots__ = ["timestamp", "root", "next_validators_hash"]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ROOT_FIELD_NUMBER: _ClassVar[int]
    NEXT_VALIDATORS_HASH_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    root: _commitment_pb2.MerkleRoot
    next_validators_hash: bytes
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., root: _Optional[_Union[_commitment_pb2.MerkleRoot, _Mapping]] = ..., next_validators_hash: _Optional[bytes] = ...) -> None: ...

class Misbehaviour(_message.Message):
    __slots__ = ["client_id", "header_1", "header_2"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    HEADER_1_FIELD_NUMBER: _ClassVar[int]
    HEADER_2_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    header_1: Header
    header_2: Header
    def __init__(self, client_id: _Optional[str] = ..., header_1: _Optional[_Union[Header, _Mapping]] = ..., header_2: _Optional[_Union[Header, _Mapping]] = ...) -> None: ...

class Header(_message.Message):
    __slots__ = ["signed_header", "validator_set", "trusted_height", "trusted_validators"]
    SIGNED_HEADER_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_SET_FIELD_NUMBER: _ClassVar[int]
    TRUSTED_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    TRUSTED_VALIDATORS_FIELD_NUMBER: _ClassVar[int]
    signed_header: _types_pb2.SignedHeader
    validator_set: _validator_pb2.ValidatorSet
    trusted_height: _client_pb2.Height
    trusted_validators: _validator_pb2.ValidatorSet
    def __init__(self, signed_header: _Optional[_Union[_types_pb2.SignedHeader, _Mapping]] = ..., validator_set: _Optional[_Union[_validator_pb2.ValidatorSet, _Mapping]] = ..., trusted_height: _Optional[_Union[_client_pb2.Height, _Mapping]] = ..., trusted_validators: _Optional[_Union[_validator_pb2.ValidatorSet, _Mapping]] = ...) -> None: ...

class Fraction(_message.Message):
    __slots__ = ["numerator", "denominator"]
    NUMERATOR_FIELD_NUMBER: _ClassVar[int]
    DENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    numerator: int
    denominator: int
    def __init__(self, numerator: _Optional[int] = ..., denominator: _Optional[int] = ...) -> None: ...
