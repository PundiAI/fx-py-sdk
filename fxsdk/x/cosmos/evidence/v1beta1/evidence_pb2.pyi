from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from fxpysdk.fxsdk.x.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Equivocation(_message.Message):
    __slots__ = ["height", "time", "power", "consensus_address"]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    CONSENSUS_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    height: int
    time: _timestamp_pb2.Timestamp
    power: int
    consensus_address: str
    def __init__(self, height: _Optional[int] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., power: _Optional[int] = ..., consensus_address: _Optional[str] = ...) -> None: ...
