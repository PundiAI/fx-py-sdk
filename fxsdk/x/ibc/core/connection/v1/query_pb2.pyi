from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from fxsdk.x.cosmos.base.query.v1beta1 import pagination_pb2 as _pagination_pb2
from fxsdk.x.ibc.core.client.v1 import client_pb2 as _client_pb2
from fxsdk.x.ibc.core.connection.v1 import connection_pb2 as _connection_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryConnectionRequest(_message.Message):
    __slots__ = ["connection_id"]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    def __init__(self, connection_id: _Optional[str] = ...) -> None: ...

class QueryConnectionResponse(_message.Message):
    __slots__ = ["connection", "proof", "proof_height"]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    PROOF_FIELD_NUMBER: _ClassVar[int]
    PROOF_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    connection: _connection_pb2.ConnectionEnd
    proof: bytes
    proof_height: _client_pb2.Height
    def __init__(self, connection: _Optional[_Union[_connection_pb2.ConnectionEnd, _Mapping]] = ..., proof: _Optional[bytes] = ..., proof_height: _Optional[_Union[_client_pb2.Height, _Mapping]] = ...) -> None: ...

class QueryConnectionsRequest(_message.Message):
    __slots__ = ["pagination"]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.PageRequest
    def __init__(self, pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryConnectionsResponse(_message.Message):
    __slots__ = ["connections", "pagination", "height"]
    CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    connections: _containers.RepeatedCompositeFieldContainer[_connection_pb2.IdentifiedConnection]
    pagination: _pagination_pb2.PageResponse
    height: _client_pb2.Height
    def __init__(self, connections: _Optional[_Iterable[_Union[_connection_pb2.IdentifiedConnection, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ..., height: _Optional[_Union[_client_pb2.Height, _Mapping]] = ...) -> None: ...

class QueryClientConnectionsRequest(_message.Message):
    __slots__ = ["client_id"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    def __init__(self, client_id: _Optional[str] = ...) -> None: ...

class QueryClientConnectionsResponse(_message.Message):
    __slots__ = ["connection_paths", "proof", "proof_height"]
    CONNECTION_PATHS_FIELD_NUMBER: _ClassVar[int]
    PROOF_FIELD_NUMBER: _ClassVar[int]
    PROOF_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    connection_paths: _containers.RepeatedScalarFieldContainer[str]
    proof: bytes
    proof_height: _client_pb2.Height
    def __init__(self, connection_paths: _Optional[_Iterable[str]] = ..., proof: _Optional[bytes] = ..., proof_height: _Optional[_Union[_client_pb2.Height, _Mapping]] = ...) -> None: ...

class QueryConnectionClientStateRequest(_message.Message):
    __slots__ = ["connection_id"]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    def __init__(self, connection_id: _Optional[str] = ...) -> None: ...

class QueryConnectionClientStateResponse(_message.Message):
    __slots__ = ["identified_client_state", "proof", "proof_height"]
    IDENTIFIED_CLIENT_STATE_FIELD_NUMBER: _ClassVar[int]
    PROOF_FIELD_NUMBER: _ClassVar[int]
    PROOF_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    identified_client_state: _client_pb2.IdentifiedClientState
    proof: bytes
    proof_height: _client_pb2.Height
    def __init__(self, identified_client_state: _Optional[_Union[_client_pb2.IdentifiedClientState, _Mapping]] = ..., proof: _Optional[bytes] = ..., proof_height: _Optional[_Union[_client_pb2.Height, _Mapping]] = ...) -> None: ...

class QueryConnectionConsensusStateRequest(_message.Message):
    __slots__ = ["connection_id", "revision_number", "revision_height"]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    REVISION_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    revision_number: int
    revision_height: int
    def __init__(self, connection_id: _Optional[str] = ..., revision_number: _Optional[int] = ..., revision_height: _Optional[int] = ...) -> None: ...

class QueryConnectionConsensusStateResponse(_message.Message):
    __slots__ = ["consensus_state", "client_id", "proof", "proof_height"]
    CONSENSUS_STATE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROOF_FIELD_NUMBER: _ClassVar[int]
    PROOF_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    consensus_state: _any_pb2.Any
    client_id: str
    proof: bytes
    proof_height: _client_pb2.Height
    def __init__(self, consensus_state: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., client_id: _Optional[str] = ..., proof: _Optional[bytes] = ..., proof_height: _Optional[_Union[_client_pb2.Height, _Mapping]] = ...) -> None: ...

class QueryConnectionParamsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryConnectionParamsResponse(_message.Message):
    __slots__ = ["params"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _connection_pb2.Params
    def __init__(self, params: _Optional[_Union[_connection_pb2.Params, _Mapping]] = ...) -> None: ...
