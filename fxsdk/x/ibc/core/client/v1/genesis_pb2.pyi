from ibc.core.client.v1 import client_pb2 as _client_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ["clients", "clients_consensus", "clients_metadata", "params", "create_localhost", "next_client_sequence"]
    CLIENTS_FIELD_NUMBER: _ClassVar[int]
    CLIENTS_CONSENSUS_FIELD_NUMBER: _ClassVar[int]
    CLIENTS_METADATA_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    CREATE_LOCALHOST_FIELD_NUMBER: _ClassVar[int]
    NEXT_CLIENT_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    clients: _containers.RepeatedCompositeFieldContainer[_client_pb2.IdentifiedClientState]
    clients_consensus: _containers.RepeatedCompositeFieldContainer[_client_pb2.ClientConsensusStates]
    clients_metadata: _containers.RepeatedCompositeFieldContainer[IdentifiedGenesisMetadata]
    params: _client_pb2.Params
    create_localhost: bool
    next_client_sequence: int
    def __init__(self, clients: _Optional[_Iterable[_Union[_client_pb2.IdentifiedClientState, _Mapping]]] = ..., clients_consensus: _Optional[_Iterable[_Union[_client_pb2.ClientConsensusStates, _Mapping]]] = ..., clients_metadata: _Optional[_Iterable[_Union[IdentifiedGenesisMetadata, _Mapping]]] = ..., params: _Optional[_Union[_client_pb2.Params, _Mapping]] = ..., create_localhost: bool = ..., next_client_sequence: _Optional[int] = ...) -> None: ...

class GenesisMetadata(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: bytes
    value: bytes
    def __init__(self, key: _Optional[bytes] = ..., value: _Optional[bytes] = ...) -> None: ...

class IdentifiedGenesisMetadata(_message.Message):
    __slots__ = ["client_id", "client_metadata"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_METADATA_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    client_metadata: _containers.RepeatedCompositeFieldContainer[GenesisMetadata]
    def __init__(self, client_id: _Optional[str] = ..., client_metadata: _Optional[_Iterable[_Union[GenesisMetadata, _Mapping]]] = ...) -> None: ...
