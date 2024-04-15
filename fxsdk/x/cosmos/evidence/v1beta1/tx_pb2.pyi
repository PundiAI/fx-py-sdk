from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import any_pb2 as _any_pb2
from fxpysdk.fxsdk.x.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from fxpysdk.fxsdk.x.cosmos.msg.v1 import msg_pb2 as _msg_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MsgSubmitEvidence(_message.Message):
    __slots__ = ["submitter", "evidence"]
    SUBMITTER_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    submitter: str
    evidence: _any_pb2.Any
    def __init__(self, submitter: _Optional[str] = ..., evidence: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class MsgSubmitEvidenceResponse(_message.Message):
    __slots__ = ["hash"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    hash: bytes
    def __init__(self, hash: _Optional[bytes] = ...) -> None: ...
