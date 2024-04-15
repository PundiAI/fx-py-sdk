from fxpysdk.fxsdk.x.cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from fxpysdk.fxsdk.x.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VoteOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    VOTE_OPTION_UNSPECIFIED: _ClassVar[VoteOption]
    VOTE_OPTION_YES: _ClassVar[VoteOption]
    VOTE_OPTION_ABSTAIN: _ClassVar[VoteOption]
    VOTE_OPTION_NO: _ClassVar[VoteOption]
    VOTE_OPTION_NO_WITH_VETO: _ClassVar[VoteOption]

class ProposalStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    PROPOSAL_STATUS_UNSPECIFIED: _ClassVar[ProposalStatus]
    PROPOSAL_STATUS_DEPOSIT_PERIOD: _ClassVar[ProposalStatus]
    PROPOSAL_STATUS_VOTING_PERIOD: _ClassVar[ProposalStatus]
    PROPOSAL_STATUS_PASSED: _ClassVar[ProposalStatus]
    PROPOSAL_STATUS_REJECTED: _ClassVar[ProposalStatus]
    PROPOSAL_STATUS_FAILED: _ClassVar[ProposalStatus]
VOTE_OPTION_UNSPECIFIED: VoteOption
VOTE_OPTION_YES: VoteOption
VOTE_OPTION_ABSTAIN: VoteOption
VOTE_OPTION_NO: VoteOption
VOTE_OPTION_NO_WITH_VETO: VoteOption
PROPOSAL_STATUS_UNSPECIFIED: ProposalStatus
PROPOSAL_STATUS_DEPOSIT_PERIOD: ProposalStatus
PROPOSAL_STATUS_VOTING_PERIOD: ProposalStatus
PROPOSAL_STATUS_PASSED: ProposalStatus
PROPOSAL_STATUS_REJECTED: ProposalStatus
PROPOSAL_STATUS_FAILED: ProposalStatus

class WeightedVoteOption(_message.Message):
    __slots__ = ["option", "weight"]
    OPTION_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    option: VoteOption
    weight: str
    def __init__(self, option: _Optional[_Union[VoteOption, str]] = ..., weight: _Optional[str] = ...) -> None: ...

class TextProposal(_message.Message):
    __slots__ = ["title", "description"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class Deposit(_message.Message):
    __slots__ = ["proposal_id", "depositor", "amount"]
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    DEPOSITOR_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    proposal_id: int
    depositor: str
    amount: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    def __init__(self, proposal_id: _Optional[int] = ..., depositor: _Optional[str] = ..., amount: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ...) -> None: ...

class Proposal(_message.Message):
    __slots__ = ["proposal_id", "content", "status", "final_tally_result", "submit_time", "deposit_end_time", "total_deposit", "voting_start_time", "voting_end_time"]
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FINAL_TALLY_RESULT_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_TIME_FIELD_NUMBER: _ClassVar[int]
    DEPOSIT_END_TIME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DEPOSIT_FIELD_NUMBER: _ClassVar[int]
    VOTING_START_TIME_FIELD_NUMBER: _ClassVar[int]
    VOTING_END_TIME_FIELD_NUMBER: _ClassVar[int]
    proposal_id: int
    content: _any_pb2.Any
    status: ProposalStatus
    final_tally_result: TallyResult
    submit_time: _timestamp_pb2.Timestamp
    deposit_end_time: _timestamp_pb2.Timestamp
    total_deposit: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    voting_start_time: _timestamp_pb2.Timestamp
    voting_end_time: _timestamp_pb2.Timestamp
    def __init__(self, proposal_id: _Optional[int] = ..., content: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., status: _Optional[_Union[ProposalStatus, str]] = ..., final_tally_result: _Optional[_Union[TallyResult, _Mapping]] = ..., submit_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deposit_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., total_deposit: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ..., voting_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., voting_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class TallyResult(_message.Message):
    __slots__ = ["yes", "abstain", "no", "no_with_veto"]
    YES_FIELD_NUMBER: _ClassVar[int]
    ABSTAIN_FIELD_NUMBER: _ClassVar[int]
    NO_FIELD_NUMBER: _ClassVar[int]
    NO_WITH_VETO_FIELD_NUMBER: _ClassVar[int]
    yes: str
    abstain: str
    no: str
    no_with_veto: str
    def __init__(self, yes: _Optional[str] = ..., abstain: _Optional[str] = ..., no: _Optional[str] = ..., no_with_veto: _Optional[str] = ...) -> None: ...

class Vote(_message.Message):
    __slots__ = ["proposal_id", "voter", "option", "options"]
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    VOTER_FIELD_NUMBER: _ClassVar[int]
    OPTION_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    proposal_id: int
    voter: str
    option: VoteOption
    options: _containers.RepeatedCompositeFieldContainer[WeightedVoteOption]
    def __init__(self, proposal_id: _Optional[int] = ..., voter: _Optional[str] = ..., option: _Optional[_Union[VoteOption, str]] = ..., options: _Optional[_Iterable[_Union[WeightedVoteOption, _Mapping]]] = ...) -> None: ...

class DepositParams(_message.Message):
    __slots__ = ["min_deposit", "max_deposit_period"]
    MIN_DEPOSIT_FIELD_NUMBER: _ClassVar[int]
    MAX_DEPOSIT_PERIOD_FIELD_NUMBER: _ClassVar[int]
    min_deposit: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    max_deposit_period: _duration_pb2.Duration
    def __init__(self, min_deposit: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ..., max_deposit_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class VotingParams(_message.Message):
    __slots__ = ["voting_period"]
    VOTING_PERIOD_FIELD_NUMBER: _ClassVar[int]
    voting_period: _duration_pb2.Duration
    def __init__(self, voting_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class TallyParams(_message.Message):
    __slots__ = ["quorum", "threshold", "veto_threshold"]
    QUORUM_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    VETO_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    quorum: bytes
    threshold: bytes
    veto_threshold: bytes
    def __init__(self, quorum: _Optional[bytes] = ..., threshold: _Optional[bytes] = ..., veto_threshold: _Optional[bytes] = ...) -> None: ...
