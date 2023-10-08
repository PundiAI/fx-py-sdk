from cosmos.group.v1 import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ["group_seq", "groups", "group_members", "group_policy_seq", "group_policies", "proposal_seq", "proposals", "votes"]
    GROUP_SEQ_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    GROUP_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    GROUP_POLICY_SEQ_FIELD_NUMBER: _ClassVar[int]
    GROUP_POLICIES_FIELD_NUMBER: _ClassVar[int]
    PROPOSAL_SEQ_FIELD_NUMBER: _ClassVar[int]
    PROPOSALS_FIELD_NUMBER: _ClassVar[int]
    VOTES_FIELD_NUMBER: _ClassVar[int]
    group_seq: int
    groups: _containers.RepeatedCompositeFieldContainer[_types_pb2.GroupInfo]
    group_members: _containers.RepeatedCompositeFieldContainer[_types_pb2.GroupMember]
    group_policy_seq: int
    group_policies: _containers.RepeatedCompositeFieldContainer[_types_pb2.GroupPolicyInfo]
    proposal_seq: int
    proposals: _containers.RepeatedCompositeFieldContainer[_types_pb2.Proposal]
    votes: _containers.RepeatedCompositeFieldContainer[_types_pb2.Vote]
    def __init__(self, group_seq: _Optional[int] = ..., groups: _Optional[_Iterable[_Union[_types_pb2.GroupInfo, _Mapping]]] = ..., group_members: _Optional[_Iterable[_Union[_types_pb2.GroupMember, _Mapping]]] = ..., group_policy_seq: _Optional[int] = ..., group_policies: _Optional[_Iterable[_Union[_types_pb2.GroupPolicyInfo, _Mapping]]] = ..., proposal_seq: _Optional[int] = ..., proposals: _Optional[_Iterable[_Union[_types_pb2.Proposal, _Mapping]]] = ..., votes: _Optional[_Iterable[_Union[_types_pb2.Vote, _Mapping]]] = ...) -> None: ...
