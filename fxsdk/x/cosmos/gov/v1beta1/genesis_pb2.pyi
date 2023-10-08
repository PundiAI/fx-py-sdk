from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos.gov.v1beta1 import gov_pb2 as _gov_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ["starting_proposal_id", "deposits", "votes", "proposals", "deposit_params", "voting_params", "tally_params"]
    STARTING_PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    DEPOSITS_FIELD_NUMBER: _ClassVar[int]
    VOTES_FIELD_NUMBER: _ClassVar[int]
    PROPOSALS_FIELD_NUMBER: _ClassVar[int]
    DEPOSIT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VOTING_PARAMS_FIELD_NUMBER: _ClassVar[int]
    TALLY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    starting_proposal_id: int
    deposits: _containers.RepeatedCompositeFieldContainer[_gov_pb2.Deposit]
    votes: _containers.RepeatedCompositeFieldContainer[_gov_pb2.Vote]
    proposals: _containers.RepeatedCompositeFieldContainer[_gov_pb2.Proposal]
    deposit_params: _gov_pb2.DepositParams
    voting_params: _gov_pb2.VotingParams
    tally_params: _gov_pb2.TallyParams
    def __init__(self, starting_proposal_id: _Optional[int] = ..., deposits: _Optional[_Iterable[_Union[_gov_pb2.Deposit, _Mapping]]] = ..., votes: _Optional[_Iterable[_Union[_gov_pb2.Vote, _Mapping]]] = ..., proposals: _Optional[_Iterable[_Union[_gov_pb2.Proposal, _Mapping]]] = ..., deposit_params: _Optional[_Union[_gov_pb2.DepositParams, _Mapping]] = ..., voting_params: _Optional[_Union[_gov_pb2.VotingParams, _Mapping]] = ..., tally_params: _Optional[_Union[_gov_pb2.TallyParams, _Mapping]] = ...) -> None: ...
