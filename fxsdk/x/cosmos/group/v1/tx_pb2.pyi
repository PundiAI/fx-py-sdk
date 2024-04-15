from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from fxpysdk.fxsdk.x.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf import any_pb2 as _any_pb2
from fxpysdk.fxsdk.x.cosmos.group.v1 import types_pb2 as _types_pb2
from fxpysdk.fxsdk.x.cosmos.msg.v1 import msg_pb2 as _msg_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Exec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    EXEC_UNSPECIFIED: _ClassVar[Exec]
    EXEC_TRY: _ClassVar[Exec]
EXEC_UNSPECIFIED: Exec
EXEC_TRY: Exec

class MsgCreateGroup(_message.Message):
    __slots__ = ["admin", "members", "metadata"]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    admin: str
    members: _containers.RepeatedCompositeFieldContainer[_types_pb2.MemberRequest]
    metadata: str
    def __init__(self, admin: _Optional[str] = ..., members: _Optional[_Iterable[_Union[_types_pb2.MemberRequest, _Mapping]]] = ..., metadata: _Optional[str] = ...) -> None: ...

class MsgCreateGroupResponse(_message.Message):
    __slots__ = ["group_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    def __init__(self, group_id: _Optional[int] = ...) -> None: ...

class MsgUpdateGroupMembers(_message.Message):
    __slots__ = ["admin", "group_id", "member_updates"]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_UPDATES_FIELD_NUMBER: _ClassVar[int]
    admin: str
    group_id: int
    member_updates: _containers.RepeatedCompositeFieldContainer[_types_pb2.MemberRequest]
    def __init__(self, admin: _Optional[str] = ..., group_id: _Optional[int] = ..., member_updates: _Optional[_Iterable[_Union[_types_pb2.MemberRequest, _Mapping]]] = ...) -> None: ...

class MsgUpdateGroupMembersResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgUpdateGroupAdmin(_message.Message):
    __slots__ = ["admin", "group_id", "new_admin"]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_ADMIN_FIELD_NUMBER: _ClassVar[int]
    admin: str
    group_id: int
    new_admin: str
    def __init__(self, admin: _Optional[str] = ..., group_id: _Optional[int] = ..., new_admin: _Optional[str] = ...) -> None: ...

class MsgUpdateGroupAdminResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgUpdateGroupMetadata(_message.Message):
    __slots__ = ["admin", "group_id", "metadata"]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    admin: str
    group_id: int
    metadata: str
    def __init__(self, admin: _Optional[str] = ..., group_id: _Optional[int] = ..., metadata: _Optional[str] = ...) -> None: ...

class MsgUpdateGroupMetadataResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgCreateGroupPolicy(_message.Message):
    __slots__ = ["admin", "group_id", "metadata", "decision_policy"]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DECISION_POLICY_FIELD_NUMBER: _ClassVar[int]
    admin: str
    group_id: int
    metadata: str
    decision_policy: _any_pb2.Any
    def __init__(self, admin: _Optional[str] = ..., group_id: _Optional[int] = ..., metadata: _Optional[str] = ..., decision_policy: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class MsgCreateGroupPolicyResponse(_message.Message):
    __slots__ = ["address"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...

class MsgUpdateGroupPolicyAdmin(_message.Message):
    __slots__ = ["admin", "group_policy_address", "new_admin"]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    GROUP_POLICY_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NEW_ADMIN_FIELD_NUMBER: _ClassVar[int]
    admin: str
    group_policy_address: str
    new_admin: str
    def __init__(self, admin: _Optional[str] = ..., group_policy_address: _Optional[str] = ..., new_admin: _Optional[str] = ...) -> None: ...

class MsgCreateGroupWithPolicy(_message.Message):
    __slots__ = ["admin", "members", "group_metadata", "group_policy_metadata", "group_policy_as_admin", "decision_policy"]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    GROUP_METADATA_FIELD_NUMBER: _ClassVar[int]
    GROUP_POLICY_METADATA_FIELD_NUMBER: _ClassVar[int]
    GROUP_POLICY_AS_ADMIN_FIELD_NUMBER: _ClassVar[int]
    DECISION_POLICY_FIELD_NUMBER: _ClassVar[int]
    admin: str
    members: _containers.RepeatedCompositeFieldContainer[_types_pb2.MemberRequest]
    group_metadata: str
    group_policy_metadata: str
    group_policy_as_admin: bool
    decision_policy: _any_pb2.Any
    def __init__(self, admin: _Optional[str] = ..., members: _Optional[_Iterable[_Union[_types_pb2.MemberRequest, _Mapping]]] = ..., group_metadata: _Optional[str] = ..., group_policy_metadata: _Optional[str] = ..., group_policy_as_admin: bool = ..., decision_policy: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class MsgCreateGroupWithPolicyResponse(_message.Message):
    __slots__ = ["group_id", "group_policy_address"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_POLICY_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    group_policy_address: str
    def __init__(self, group_id: _Optional[int] = ..., group_policy_address: _Optional[str] = ...) -> None: ...

class MsgUpdateGroupPolicyAdminResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgUpdateGroupPolicyDecisionPolicy(_message.Message):
    __slots__ = ["admin", "group_policy_address", "decision_policy"]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    GROUP_POLICY_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DECISION_POLICY_FIELD_NUMBER: _ClassVar[int]
    admin: str
    group_policy_address: str
    decision_policy: _any_pb2.Any
    def __init__(self, admin: _Optional[str] = ..., group_policy_address: _Optional[str] = ..., decision_policy: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class MsgUpdateGroupPolicyDecisionPolicyResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgUpdateGroupPolicyMetadata(_message.Message):
    __slots__ = ["admin", "group_policy_address", "metadata"]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    GROUP_POLICY_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    admin: str
    group_policy_address: str
    metadata: str
    def __init__(self, admin: _Optional[str] = ..., group_policy_address: _Optional[str] = ..., metadata: _Optional[str] = ...) -> None: ...

class MsgUpdateGroupPolicyMetadataResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgSubmitProposal(_message.Message):
    __slots__ = ["group_policy_address", "proposers", "metadata", "messages", "exec"]
    GROUP_POLICY_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PROPOSERS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    EXEC_FIELD_NUMBER: _ClassVar[int]
    group_policy_address: str
    proposers: _containers.RepeatedScalarFieldContainer[str]
    metadata: str
    messages: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    exec: Exec
    def __init__(self, group_policy_address: _Optional[str] = ..., proposers: _Optional[_Iterable[str]] = ..., metadata: _Optional[str] = ..., messages: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ..., exec: _Optional[_Union[Exec, str]] = ...) -> None: ...

class MsgSubmitProposalResponse(_message.Message):
    __slots__ = ["proposal_id"]
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    proposal_id: int
    def __init__(self, proposal_id: _Optional[int] = ...) -> None: ...

class MsgWithdrawProposal(_message.Message):
    __slots__ = ["proposal_id", "address"]
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    proposal_id: int
    address: str
    def __init__(self, proposal_id: _Optional[int] = ..., address: _Optional[str] = ...) -> None: ...

class MsgWithdrawProposalResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgVote(_message.Message):
    __slots__ = ["proposal_id", "voter", "option", "metadata", "exec"]
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    VOTER_FIELD_NUMBER: _ClassVar[int]
    OPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    EXEC_FIELD_NUMBER: _ClassVar[int]
    proposal_id: int
    voter: str
    option: _types_pb2.VoteOption
    metadata: str
    exec: Exec
    def __init__(self, proposal_id: _Optional[int] = ..., voter: _Optional[str] = ..., option: _Optional[_Union[_types_pb2.VoteOption, str]] = ..., metadata: _Optional[str] = ..., exec: _Optional[_Union[Exec, str]] = ...) -> None: ...

class MsgVoteResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgExec(_message.Message):
    __slots__ = ["proposal_id", "executor"]
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTOR_FIELD_NUMBER: _ClassVar[int]
    proposal_id: int
    executor: str
    def __init__(self, proposal_id: _Optional[int] = ..., executor: _Optional[str] = ...) -> None: ...

class MsgExecResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _types_pb2.ProposalExecutorResult
    def __init__(self, result: _Optional[_Union[_types_pb2.ProposalExecutorResult, str]] = ...) -> None: ...

class MsgLeaveGroup(_message.Message):
    __slots__ = ["address", "group_id"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    address: str
    group_id: int
    def __init__(self, address: _Optional[str] = ..., group_id: _Optional[int] = ...) -> None: ...

class MsgLeaveGroupResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
