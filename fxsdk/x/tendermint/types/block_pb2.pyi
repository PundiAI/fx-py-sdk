from gogoproto import gogo_pb2 as _gogo_pb2
from tendermint.types import types_pb2 as _types_pb2
from tendermint.types import evidence_pb2 as _evidence_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Block(_message.Message):
    __slots__ = ["header", "data", "evidence", "last_commit"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    LAST_COMMIT_FIELD_NUMBER: _ClassVar[int]
    header: _types_pb2.Header
    data: _types_pb2.Data
    evidence: _evidence_pb2.EvidenceList
    last_commit: _types_pb2.Commit
    def __init__(self, header: _Optional[_Union[_types_pb2.Header, _Mapping]] = ..., data: _Optional[_Union[_types_pb2.Data, _Mapping]] = ..., evidence: _Optional[_Union[_evidence_pb2.EvidenceList, _Mapping]] = ..., last_commit: _Optional[_Union[_types_pb2.Commit, _Mapping]] = ...) -> None: ...
