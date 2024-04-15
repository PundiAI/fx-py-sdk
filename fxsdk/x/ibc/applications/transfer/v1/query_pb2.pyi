from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from fxpysdk.fxsdk.x.cosmos.base.query.v1beta1 import pagination_pb2 as _pagination_pb2
from fxpysdk.fxsdk.x.ibc.applications.transfer.v1 import transfer_pb2 as _transfer_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryDenomTraceRequest(_message.Message):
    __slots__ = ["hash"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    hash: str
    def __init__(self, hash: _Optional[str] = ...) -> None: ...

class QueryDenomTraceResponse(_message.Message):
    __slots__ = ["denom_trace"]
    DENOM_TRACE_FIELD_NUMBER: _ClassVar[int]
    denom_trace: _transfer_pb2.DenomTrace
    def __init__(self, denom_trace: _Optional[_Union[_transfer_pb2.DenomTrace, _Mapping]] = ...) -> None: ...

class QueryDenomTracesRequest(_message.Message):
    __slots__ = ["pagination"]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.PageRequest
    def __init__(self, pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryDenomTracesResponse(_message.Message):
    __slots__ = ["denom_traces", "pagination"]
    DENOM_TRACES_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    denom_traces: _containers.RepeatedCompositeFieldContainer[_transfer_pb2.DenomTrace]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, denom_traces: _Optional[_Iterable[_Union[_transfer_pb2.DenomTrace, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class QueryParamsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryParamsResponse(_message.Message):
    __slots__ = ["params"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _transfer_pb2.Params
    def __init__(self, params: _Optional[_Union[_transfer_pb2.Params, _Mapping]] = ...) -> None: ...

class QueryDenomHashRequest(_message.Message):
    __slots__ = ["trace"]
    TRACE_FIELD_NUMBER: _ClassVar[int]
    trace: str
    def __init__(self, trace: _Optional[str] = ...) -> None: ...

class QueryDenomHashResponse(_message.Message):
    __slots__ = ["hash"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    hash: str
    def __init__(self, hash: _Optional[str] = ...) -> None: ...

class QueryEscrowAddressRequest(_message.Message):
    __slots__ = ["port_id", "channel_id"]
    PORT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    port_id: str
    channel_id: str
    def __init__(self, port_id: _Optional[str] = ..., channel_id: _Optional[str] = ...) -> None: ...

class QueryEscrowAddressResponse(_message.Message):
    __slots__ = ["escrow_address"]
    ESCROW_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    escrow_address: str
    def __init__(self, escrow_address: _Optional[str] = ...) -> None: ...
