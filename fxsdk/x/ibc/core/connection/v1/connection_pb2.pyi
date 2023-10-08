from gogoproto import gogo_pb2 as _gogo_pb2
from ibc.core.commitment.v1 import commitment_pb2 as _commitment_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    STATE_UNINITIALIZED_UNSPECIFIED: _ClassVar[State]
    STATE_INIT: _ClassVar[State]
    STATE_TRYOPEN: _ClassVar[State]
    STATE_OPEN: _ClassVar[State]
STATE_UNINITIALIZED_UNSPECIFIED: State
STATE_INIT: State
STATE_TRYOPEN: State
STATE_OPEN: State

class ConnectionEnd(_message.Message):
    __slots__ = ["client_id", "versions", "state", "counterparty", "delay_period"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    COUNTERPARTY_FIELD_NUMBER: _ClassVar[int]
    DELAY_PERIOD_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    versions: _containers.RepeatedCompositeFieldContainer[Version]
    state: State
    counterparty: Counterparty
    delay_period: int
    def __init__(self, client_id: _Optional[str] = ..., versions: _Optional[_Iterable[_Union[Version, _Mapping]]] = ..., state: _Optional[_Union[State, str]] = ..., counterparty: _Optional[_Union[Counterparty, _Mapping]] = ..., delay_period: _Optional[int] = ...) -> None: ...

class IdentifiedConnection(_message.Message):
    __slots__ = ["id", "client_id", "versions", "state", "counterparty", "delay_period"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    COUNTERPARTY_FIELD_NUMBER: _ClassVar[int]
    DELAY_PERIOD_FIELD_NUMBER: _ClassVar[int]
    id: str
    client_id: str
    versions: _containers.RepeatedCompositeFieldContainer[Version]
    state: State
    counterparty: Counterparty
    delay_period: int
    def __init__(self, id: _Optional[str] = ..., client_id: _Optional[str] = ..., versions: _Optional[_Iterable[_Union[Version, _Mapping]]] = ..., state: _Optional[_Union[State, str]] = ..., counterparty: _Optional[_Union[Counterparty, _Mapping]] = ..., delay_period: _Optional[int] = ...) -> None: ...

class Counterparty(_message.Message):
    __slots__ = ["client_id", "connection_id", "prefix"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    connection_id: str
    prefix: _commitment_pb2.MerklePrefix
    def __init__(self, client_id: _Optional[str] = ..., connection_id: _Optional[str] = ..., prefix: _Optional[_Union[_commitment_pb2.MerklePrefix, _Mapping]] = ...) -> None: ...

class ClientPaths(_message.Message):
    __slots__ = ["paths"]
    PATHS_FIELD_NUMBER: _ClassVar[int]
    paths: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, paths: _Optional[_Iterable[str]] = ...) -> None: ...

class ConnectionPaths(_message.Message):
    __slots__ = ["client_id", "paths"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    PATHS_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    paths: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, client_id: _Optional[str] = ..., paths: _Optional[_Iterable[str]] = ...) -> None: ...

class Version(_message.Message):
    __slots__ = ["identifier", "features"]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    identifier: str
    features: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, identifier: _Optional[str] = ..., features: _Optional[_Iterable[str]] = ...) -> None: ...

class Params(_message.Message):
    __slots__ = ["max_expected_time_per_block"]
    MAX_EXPECTED_TIME_PER_BLOCK_FIELD_NUMBER: _ClassVar[int]
    max_expected_time_per_block: int
    def __init__(self, max_expected_time_per_block: _Optional[int] = ...) -> None: ...
