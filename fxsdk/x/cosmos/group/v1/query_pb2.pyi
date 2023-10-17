from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.api import annotations_pb2 as _annotations_pb2
from fxsdk.x.cosmos.group.v1 import types_pb2 as _types_pb2
from fxsdk.x.cosmos.base.query.v1beta1 import pagination_pb2 as _pagination_pb2
from fxsdk.x.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryGroupInfoRequest(_message.Message):
    __slots__ = ["group_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    def __init__(self, group_id: _Optional[int] = ...) -> None: ...

class QueryGroupInfoResponse(_message.Message):
    __slots__ = ["info"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: _types_pb2.GroupInfo
    def __init__(self, info: _Optional[_Union[_types_pb2.GroupInfo, _Mapping]] = ...) -> None: ...

class QueryGroupPolicyInfoRequest(_message.Message):
    __slots__ = ["address"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...

class QueryGroupPolicyInfoResponse(_message.Message):
    __slots__ = ["info"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: _types_pb2.GroupPolicyInfo
    def __init__(self, info: _Optional[_Union[_types_pb2.GroupPolicyInfo, _Mapping]] = ...) -> None: ...

class QueryGroupMembersRequest(_message.Message):
    __slots__ = ["group_id", "pagination"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    pagination: _pagination_pb2.PageRequest
    def __init__(self, group_id: _Optional[int] = ..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryGroupMembersResponse(_message.Message):
    __slots__ = ["members", "pagination"]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    members: _containers.RepeatedCompositeFieldContainer[_types_pb2.GroupMember]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, members: _Optional[_Iterable[_Union[_types_pb2.GroupMember, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class QueryGroupsByAdminRequest(_message.Message):
    __slots__ = ["admin", "pagination"]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    admin: str
    pagination: _pagination_pb2.PageRequest
    def __init__(self, admin: _Optional[str] = ..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryGroupsByAdminResponse(_message.Message):
    __slots__ = ["groups", "pagination"]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[_types_pb2.GroupInfo]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, groups: _Optional[_Iterable[_Union[_types_pb2.GroupInfo, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class QueryGroupPoliciesByGroupRequest(_message.Message):
    __slots__ = ["group_id", "pagination"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    pagination: _pagination_pb2.PageRequest
    def __init__(self, group_id: _Optional[int] = ..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryGroupPoliciesByGroupResponse(_message.Message):
    __slots__ = ["group_policies", "pagination"]
    GROUP_POLICIES_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    group_policies: _containers.RepeatedCompositeFieldContainer[_types_pb2.GroupPolicyInfo]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, group_policies: _Optional[_Iterable[_Union[_types_pb2.GroupPolicyInfo, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class QueryGroupPoliciesByAdminRequest(_message.Message):
    __slots__ = ["admin", "pagination"]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    admin: str
    pagination: _pagination_pb2.PageRequest
    def __init__(self, admin: _Optional[str] = ..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryGroupPoliciesByAdminResponse(_message.Message):
    __slots__ = ["group_policies", "pagination"]
    GROUP_POLICIES_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    group_policies: _containers.RepeatedCompositeFieldContainer[_types_pb2.GroupPolicyInfo]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, group_policies: _Optional[_Iterable[_Union[_types_pb2.GroupPolicyInfo, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class QueryProposalRequest(_message.Message):
    __slots__ = ["proposal_id"]
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    proposal_id: int
    def __init__(self, proposal_id: _Optional[int] = ...) -> None: ...

class QueryProposalResponse(_message.Message):
    __slots__ = ["proposal"]
    PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    proposal: _types_pb2.Proposal
    def __init__(self, proposal: _Optional[_Union[_types_pb2.Proposal, _Mapping]] = ...) -> None: ...

class QueryProposalsByGroupPolicyRequest(_message.Message):
    __slots__ = ["address", "pagination"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    address: str
    pagination: _pagination_pb2.PageRequest
    def __init__(self, address: _Optional[str] = ..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryProposalsByGroupPolicyResponse(_message.Message):
    __slots__ = ["proposals", "pagination"]
    PROPOSALS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    proposals: _containers.RepeatedCompositeFieldContainer[_types_pb2.Proposal]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, proposals: _Optional[_Iterable[_Union[_types_pb2.Proposal, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class QueryVoteByProposalVoterRequest(_message.Message):
    __slots__ = ["proposal_id", "voter"]
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    VOTER_FIELD_NUMBER: _ClassVar[int]
    proposal_id: int
    voter: str
    def __init__(self, proposal_id: _Optional[int] = ..., voter: _Optional[str] = ...) -> None: ...

class QueryVoteByProposalVoterResponse(_message.Message):
    __slots__ = ["vote"]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    vote: _types_pb2.Vote
    def __init__(self, vote: _Optional[_Union[_types_pb2.Vote, _Mapping]] = ...) -> None: ...

class QueryVotesByProposalRequest(_message.Message):
    __slots__ = ["proposal_id", "pagination"]
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    proposal_id: int
    pagination: _pagination_pb2.PageRequest
    def __init__(self, proposal_id: _Optional[int] = ..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryVotesByProposalResponse(_message.Message):
    __slots__ = ["votes", "pagination"]
    VOTES_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    votes: _containers.RepeatedCompositeFieldContainer[_types_pb2.Vote]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, votes: _Optional[_Iterable[_Union[_types_pb2.Vote, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class QueryVotesByVoterRequest(_message.Message):
    __slots__ = ["voter", "pagination"]
    VOTER_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    voter: str
    pagination: _pagination_pb2.PageRequest
    def __init__(self, voter: _Optional[str] = ..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryVotesByVoterResponse(_message.Message):
    __slots__ = ["votes", "pagination"]
    VOTES_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    votes: _containers.RepeatedCompositeFieldContainer[_types_pb2.Vote]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, votes: _Optional[_Iterable[_Union[_types_pb2.Vote, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class QueryGroupsByMemberRequest(_message.Message):
    __slots__ = ["address", "pagination"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    address: str
    pagination: _pagination_pb2.PageRequest
    def __init__(self, address: _Optional[str] = ..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryGroupsByMemberResponse(_message.Message):
    __slots__ = ["groups", "pagination"]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[_types_pb2.GroupInfo]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, groups: _Optional[_Iterable[_Union[_types_pb2.GroupInfo, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class QueryTallyResultRequest(_message.Message):
    __slots__ = ["proposal_id"]
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    proposal_id: int
    def __init__(self, proposal_id: _Optional[int] = ...) -> None: ...

class QueryTallyResultResponse(_message.Message):
    __slots__ = ["tally"]
    TALLY_FIELD_NUMBER: _ClassVar[int]
    tally: _types_pb2.TallyResult
    def __init__(self, tally: _Optional[_Union[_types_pb2.TallyResult, _Mapping]] = ...) -> None: ...

class QueryGroupsRequest(_message.Message):
    __slots__ = ["pagination"]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.PageRequest
    def __init__(self, pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryGroupsResponse(_message.Message):
    __slots__ = ["groups", "pagination"]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[_types_pb2.GroupInfo]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, groups: _Optional[_Iterable[_Union[_types_pb2.GroupInfo, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...
