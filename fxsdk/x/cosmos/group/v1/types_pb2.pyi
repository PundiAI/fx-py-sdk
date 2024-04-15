from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from fxpysdk.fxsdk.x.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf import any_pb2 as _any_pb2
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
    PROPOSAL_STATUS_SUBMITTED: _ClassVar[ProposalStatus]
    PROPOSAL_STATUS_ACCEPTED: _ClassVar[ProposalStatus]
    PROPOSAL_STATUS_REJECTED: _ClassVar[ProposalStatus]
    PROPOSAL_STATUS_ABORTED: _ClassVar[ProposalStatus]
    PROPOSAL_STATUS_WITHDRAWN: _ClassVar[ProposalStatus]

class ProposalExecutorResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    PROPOSAL_EXECUTOR_RESULT_UNSPECIFIED: _ClassVar[ProposalExecutorResult]
    PROPOSAL_EXECUTOR_RESULT_NOT_RUN: _ClassVar[ProposalExecutorResult]
    PROPOSAL_EXECUTOR_RESULT_SUCCESS: _ClassVar[ProposalExecutorResult]
    PROPOSAL_EXECUTOR_RESULT_FAILURE: _ClassVar[ProposalExecutorResult]
VOTE_OPTION_UNSPECIFIED: VoteOption
VOTE_OPTION_YES: VoteOption
VOTE_OPTION_ABSTAIN: VoteOption
VOTE_OPTION_NO: VoteOption
VOTE_OPTION_NO_WITH_VETO: VoteOption
PROPOSAL_STATUS_UNSPECIFIED: ProposalStatus
PROPOSAL_STATUS_SUBMITTED: ProposalStatus
PROPOSAL_STATUS_ACCEPTED: ProposalStatus
PROPOSAL_STATUS_REJECTED: ProposalStatus
PROPOSAL_STATUS_ABORTED: ProposalStatus
PROPOSAL_STATUS_WITHDRAWN: ProposalStatus
PROPOSAL_EXECUTOR_RESULT_UNSPECIFIED: ProposalExecutorResult
PROPOSAL_EXECUTOR_RESULT_NOT_RUN: ProposalExecutorResult
PROPOSAL_EXECUTOR_RESULT_SUCCESS: ProposalExecutorResult
PROPOSAL_EXECUTOR_RESULT_FAILURE: ProposalExecutorResult

class Member(_message.Message):
    __slots__ = ["address", "weight", "metadata", "added_at"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ADDED_AT_FIELD_NUMBER: _ClassVar[int]
    address: str
    weight: str
    metadata: str
    added_at: _timestamp_pb2.Timestamp
    def __init__(self, address: _Optional[str] = ..., weight: _Optional[str] = ..., metadata: _Optional[str] = ..., added_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class MemberRequest(_message.Message):
    __slots__ = ["address", "weight", "metadata"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    address: str
    weight: str
    metadata: str
    def __init__(self, address: _Optional[str] = ..., weight: _Optional[str] = ..., metadata: _Optional[str] = ...) -> None: ...

class ThresholdDecisionPolicy(_message.Message):
    __slots__ = ["threshold", "windows"]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    WINDOWS_FIELD_NUMBER: _ClassVar[int]
    threshold: str
    windows: DecisionPolicyWindows
    def __init__(self, threshold: _Optional[str] = ..., windows: _Optional[_Union[DecisionPolicyWindows, _Mapping]] = ...) -> None: ...

class PercentageDecisionPolicy(_message.Message):
    __slots__ = ["percentage", "windows"]
    PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    WINDOWS_FIELD_NUMBER: _ClassVar[int]
    percentage: str
    windows: DecisionPolicyWindows
    def __init__(self, percentage: _Optional[str] = ..., windows: _Optional[_Union[DecisionPolicyWindows, _Mapping]] = ...) -> None: ...

class DecisionPolicyWindows(_message.Message):
    __slots__ = ["voting_period", "min_execution_period"]
    VOTING_PERIOD_FIELD_NUMBER: _ClassVar[int]
    MIN_EXECUTION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    voting_period: _duration_pb2.Duration
    min_execution_period: _duration_pb2.Duration
    def __init__(self, voting_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., min_execution_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class GroupInfo(_message.Message):
    __slots__ = ["id", "admin", "metadata", "version", "total_weight", "created_at"]
    ID_FIELD_NUMBER: _ClassVar[int]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TOTAL_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    admin: str
    metadata: str
    version: int
    total_weight: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., admin: _Optional[str] = ..., metadata: _Optional[str] = ..., version: _Optional[int] = ..., total_weight: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GroupMember(_message.Message):
    __slots__ = ["group_id", "member"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    member: Member
    def __init__(self, group_id: _Optional[int] = ..., member: _Optional[_Union[Member, _Mapping]] = ...) -> None: ...

class GroupPolicyInfo(_message.Message):
    __slots__ = ["address", "group_id", "admin", "metadata", "version", "decision_policy", "created_at"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DECISION_POLICY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    address: str
    group_id: int
    admin: str
    metadata: str
    version: int
    decision_policy: _any_pb2.Any
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, address: _Optional[str] = ..., group_id: _Optional[int] = ..., admin: _Optional[str] = ..., metadata: _Optional[str] = ..., version: _Optional[int] = ..., decision_policy: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Proposal(_message.Message):
    __slots__ = ["id", "group_policy_address", "metadata", "proposers", "submit_time", "group_version", "group_policy_version", "status", "final_tally_result", "voting_period_end", "executor_result", "messages"]
    ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_POLICY_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    PROPOSERS_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_TIME_FIELD_NUMBER: _ClassVar[int]
    GROUP_VERSION_FIELD_NUMBER: _ClassVar[int]
    GROUP_POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FINAL_TALLY_RESULT_FIELD_NUMBER: _ClassVar[int]
    VOTING_PERIOD_END_FIELD_NUMBER: _ClassVar[int]
    EXECUTOR_RESULT_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    id: int
    group_policy_address: str
    metadata: str
    proposers: _containers.RepeatedScalarFieldContainer[str]
    submit_time: _timestamp_pb2.Timestamp
    group_version: int
    group_policy_version: int
    status: ProposalStatus
    final_tally_result: TallyResult
    voting_period_end: _timestamp_pb2.Timestamp
    executor_result: ProposalExecutorResult
    messages: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, id: _Optional[int] = ..., group_policy_address: _Optional[str] = ..., metadata: _Optional[str] = ..., proposers: _Optional[_Iterable[str]] = ..., submit_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., group_version: _Optional[int] = ..., group_policy_version: _Optional[int] = ..., status: _Optional[_Union[ProposalStatus, str]] = ..., final_tally_result: _Optional[_Union[TallyResult, _Mapping]] = ..., voting_period_end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., executor_result: _Optional[_Union[ProposalExecutorResult, str]] = ..., messages: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class TallyResult(_message.Message):
    __slots__ = ["yes_count", "abstain_count", "no_count", "no_with_veto_count"]
    YES_COUNT_FIELD_NUMBER: _ClassVar[int]
    ABSTAIN_COUNT_FIELD_NUMBER: _ClassVar[int]
    NO_COUNT_FIELD_NUMBER: _ClassVar[int]
    NO_WITH_VETO_COUNT_FIELD_NUMBER: _ClassVar[int]
    yes_count: str
    abstain_count: str
    no_count: str
    no_with_veto_count: str
    def __init__(self, yes_count: _Optional[str] = ..., abstain_count: _Optional[str] = ..., no_count: _Optional[str] = ..., no_with_veto_count: _Optional[str] = ...) -> None: ...

class Vote(_message.Message):
    __slots__ = ["proposal_id", "voter", "option", "metadata", "submit_time"]
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    VOTER_FIELD_NUMBER: _ClassVar[int]
    OPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_TIME_FIELD_NUMBER: _ClassVar[int]
    proposal_id: int
    voter: str
    option: VoteOption
    metadata: str
    submit_time: _timestamp_pb2.Timestamp
    def __init__(self, proposal_id: _Optional[int] = ..., voter: _Optional[str] = ..., option: _Optional[_Union[VoteOption, str]] = ..., metadata: _Optional[str] = ..., submit_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
