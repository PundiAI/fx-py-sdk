from fxsdk.x.ibc.applications.transfer.v1 import transfer_pb2 as _transfer_pb2
from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ["port_id", "denom_traces", "params"]
    PORT_ID_FIELD_NUMBER: _ClassVar[int]
    DENOM_TRACES_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    port_id: str
    denom_traces: _containers.RepeatedCompositeFieldContainer[_transfer_pb2.DenomTrace]
    params: _transfer_pb2.Params
    def __init__(self, port_id: _Optional[str] = ..., denom_traces: _Optional[_Iterable[_Union[_transfer_pb2.DenomTrace, _Mapping]]] = ..., params: _Optional[_Union[_transfer_pb2.Params, _Mapping]] = ...) -> None: ...
