from fxsdk.x.cosmos.base.query.v1beta1 import pagination_pb2 as _pagination_pb2
from fxsdk.x.ibc.core.client.v1 import client_pb2 as _client_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.api import annotations_pb2 as _annotations_pb2
from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryClientStateRequest(_message.Message):
    __slots__ = ["client_id"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    def __init__(self, client_id: _Optional[str] = ...) -> None: ...

class QueryClientStateResponse(_message.Message):
    __slots__ = ["client_state", "proof", "proof_height"]
    CLIENT_STATE_FIELD_NUMBER: _ClassVar[int]
    PROOF_FIELD_NUMBER: _ClassVar[int]
    PROOF_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    client_state: _any_pb2.Any
    proof: bytes
    proof_height: _client_pb2.Height
    def __init__(self, client_state: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., proof: _Optional[bytes] = ..., proof_height: _Optional[_Union[_client_pb2.Height, _Mapping]] = ...) -> None: ...

class QueryClientStatesRequest(_message.Message):
    __slots__ = ["pagination"]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.PageRequest
    def __init__(self, pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryClientStatesResponse(_message.Message):
    __slots__ = ["client_states", "pagination"]
    CLIENT_STATES_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    client_states: _containers.RepeatedCompositeFieldContainer[_client_pb2.IdentifiedClientState]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, client_states: _Optional[_Iterable[_Union[_client_pb2.IdentifiedClientState, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class QueryConsensusStateRequest(_message.Message):
    __slots__ = ["client_id", "revision_number", "revision_height", "latest_height"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    REVISION_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    LATEST_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    revision_number: int
    revision_height: int
    latest_height: bool
    def __init__(self, client_id: _Optional[str] = ..., revision_number: _Optional[int] = ..., revision_height: _Optional[int] = ..., latest_height: bool = ...) -> None: ...

class QueryConsensusStateResponse(_message.Message):
    __slots__ = ["consensus_state", "proof", "proof_height"]
    CONSENSUS_STATE_FIELD_NUMBER: _ClassVar[int]
    PROOF_FIELD_NUMBER: _ClassVar[int]
    PROOF_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    consensus_state: _any_pb2.Any
    proof: bytes
    proof_height: _client_pb2.Height
    def __init__(self, consensus_state: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., proof: _Optional[bytes] = ..., proof_height: _Optional[_Union[_client_pb2.Height, _Mapping]] = ...) -> None: ...

class QueryConsensusStatesRequest(_message.Message):
    __slots__ = ["client_id", "pagination"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    pagination: _pagination_pb2.PageRequest
    def __init__(self, client_id: _Optional[str] = ..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryConsensusStatesResponse(_message.Message):
    __slots__ = ["consensus_states", "pagination"]
    CONSENSUS_STATES_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    consensus_states: _containers.RepeatedCompositeFieldContainer[_client_pb2.ConsensusStateWithHeight]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, consensus_states: _Optional[_Iterable[_Union[_client_pb2.ConsensusStateWithHeight, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class QueryConsensusStateHeightsRequest(_message.Message):
    __slots__ = ["client_id", "pagination"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    pagination: _pagination_pb2.PageRequest
    def __init__(self, client_id: _Optional[str] = ..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryConsensusStateHeightsResponse(_message.Message):
    __slots__ = ["consensus_state_heights", "pagination"]
    CONSENSUS_STATE_HEIGHTS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    consensus_state_heights: _containers.RepeatedCompositeFieldContainer[_client_pb2.Height]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, consensus_state_heights: _Optional[_Iterable[_Union[_client_pb2.Height, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class QueryClientStatusRequest(_message.Message):
    __slots__ = ["client_id"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    def __init__(self, client_id: _Optional[str] = ...) -> None: ...

class QueryClientStatusResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class QueryClientParamsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryClientParamsResponse(_message.Message):
    __slots__ = ["params"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _client_pb2.Params
    def __init__(self, params: _Optional[_Union[_client_pb2.Params, _Mapping]] = ...) -> None: ...

class QueryUpgradedClientStateRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryUpgradedClientStateResponse(_message.Message):
    __slots__ = ["upgraded_client_state"]
    UPGRADED_CLIENT_STATE_FIELD_NUMBER: _ClassVar[int]
    upgraded_client_state: _any_pb2.Any
    def __init__(self, upgraded_client_state: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class QueryUpgradedConsensusStateRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryUpgradedConsensusStateResponse(_message.Message):
    __slots__ = ["upgraded_consensus_state"]
    UPGRADED_CONSENSUS_STATE_FIELD_NUMBER: _ClassVar[int]
    upgraded_consensus_state: _any_pb2.Any
    def __init__(self, upgraded_consensus_state: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
