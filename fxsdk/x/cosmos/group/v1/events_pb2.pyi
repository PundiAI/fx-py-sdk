from fxpysdk.fxsdk.x.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from fxpysdk.fxsdk.x.cosmos.group.v1 import types_pb2 as _types_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EventCreateGroup(_message.Message):
    __slots__ = ["group_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    def __init__(self, group_id: _Optional[int] = ...) -> None: ...

class EventUpdateGroup(_message.Message):
    __slots__ = ["group_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    def __init__(self, group_id: _Optional[int] = ...) -> None: ...

class EventCreateGroupPolicy(_message.Message):
    __slots__ = ["address"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...

class EventUpdateGroupPolicy(_message.Message):
    __slots__ = ["address"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...

class EventSubmitProposal(_message.Message):
    __slots__ = ["proposal_id"]
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    proposal_id: int
    def __init__(self, proposal_id: _Optional[int] = ...) -> None: ...

class EventWithdrawProposal(_message.Message):
    __slots__ = ["proposal_id"]
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    proposal_id: int
    def __init__(self, proposal_id: _Optional[int] = ...) -> None: ...

class EventVote(_message.Message):
    __slots__ = ["proposal_id"]
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    proposal_id: int
    def __init__(self, proposal_id: _Optional[int] = ...) -> None: ...

class EventExec(_message.Message):
    __slots__ = ["proposal_id", "result", "logs"]
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    proposal_id: int
    result: _types_pb2.ProposalExecutorResult
    logs: str
    def __init__(self, proposal_id: _Optional[int] = ..., result: _Optional[_Union[_types_pb2.ProposalExecutorResult, str]] = ..., logs: _Optional[str] = ...) -> None: ...

class EventLeaveGroup(_message.Message):
    __slots__ = ["group_id", "address"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    address: str
    def __init__(self, group_id: _Optional[int] = ..., address: _Optional[str] = ...) -> None: ...

class EventProposalPruned(_message.Message):
    __slots__ = ["proposal_id", "status", "tally_result"]
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TALLY_RESULT_FIELD_NUMBER: _ClassVar[int]
    proposal_id: int
    status: _types_pb2.ProposalStatus
    tally_result: _types_pb2.TallyResult
    def __init__(self, proposal_id: _Optional[int] = ..., status: _Optional[_Union[_types_pb2.ProposalStatus, str]] = ..., tally_result: _Optional[_Union[_types_pb2.TallyResult, _Mapping]] = ...) -> None: ...
