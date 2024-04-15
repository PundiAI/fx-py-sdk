from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from fxpysdk.fxsdk.x.ibc.core.connection.v1 import connection_pb2 as _connection_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ["connections", "client_connection_paths", "next_connection_sequence", "params"]
    CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CONNECTION_PATHS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CONNECTION_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    connections: _containers.RepeatedCompositeFieldContainer[_connection_pb2.IdentifiedConnection]
    client_connection_paths: _containers.RepeatedCompositeFieldContainer[_connection_pb2.ConnectionPaths]
    next_connection_sequence: int
    params: _connection_pb2.Params
    def __init__(self, connections: _Optional[_Iterable[_Union[_connection_pb2.IdentifiedConnection, _Mapping]]] = ..., client_connection_paths: _Optional[_Iterable[_Union[_connection_pb2.ConnectionPaths, _Mapping]]] = ..., next_connection_sequence: _Optional[int] = ..., params: _Optional[_Union[_connection_pb2.Params, _Mapping]] = ...) -> None: ...
