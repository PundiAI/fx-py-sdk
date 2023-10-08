from gogoproto import gogo_pb2 as _gogo_pb2
from ibc.core.client.v1 import client_pb2 as _client_pb2
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
    STATE_CLOSED: _ClassVar[State]

class Order(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ORDER_NONE_UNSPECIFIED: _ClassVar[Order]
    ORDER_UNORDERED: _ClassVar[Order]
    ORDER_ORDERED: _ClassVar[Order]
STATE_UNINITIALIZED_UNSPECIFIED: State
STATE_INIT: State
STATE_TRYOPEN: State
STATE_OPEN: State
STATE_CLOSED: State
ORDER_NONE_UNSPECIFIED: Order
ORDER_UNORDERED: Order
ORDER_ORDERED: Order

class Channel(_message.Message):
    __slots__ = ["state", "ordering", "counterparty", "connection_hops", "version"]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ORDERING_FIELD_NUMBER: _ClassVar[int]
    COUNTERPARTY_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_HOPS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    state: State
    ordering: Order
    counterparty: Counterparty
    connection_hops: _containers.RepeatedScalarFieldContainer[str]
    version: str
    def __init__(self, state: _Optional[_Union[State, str]] = ..., ordering: _Optional[_Union[Order, str]] = ..., counterparty: _Optional[_Union[Counterparty, _Mapping]] = ..., connection_hops: _Optional[_Iterable[str]] = ..., version: _Optional[str] = ...) -> None: ...

class IdentifiedChannel(_message.Message):
    __slots__ = ["state", "ordering", "counterparty", "connection_hops", "version", "port_id", "channel_id"]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ORDERING_FIELD_NUMBER: _ClassVar[int]
    COUNTERPARTY_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_HOPS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    PORT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    state: State
    ordering: Order
    counterparty: Counterparty
    connection_hops: _containers.RepeatedScalarFieldContainer[str]
    version: str
    port_id: str
    channel_id: str
    def __init__(self, state: _Optional[_Union[State, str]] = ..., ordering: _Optional[_Union[Order, str]] = ..., counterparty: _Optional[_Union[Counterparty, _Mapping]] = ..., connection_hops: _Optional[_Iterable[str]] = ..., version: _Optional[str] = ..., port_id: _Optional[str] = ..., channel_id: _Optional[str] = ...) -> None: ...

class Counterparty(_message.Message):
    __slots__ = ["port_id", "channel_id"]
    PORT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    port_id: str
    channel_id: str
    def __init__(self, port_id: _Optional[str] = ..., channel_id: _Optional[str] = ...) -> None: ...

class Packet(_message.Message):
    __slots__ = ["sequence", "source_port", "source_channel", "destination_port", "destination_channel", "data", "timeout_height", "timeout_timestamp"]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PORT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PORT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    sequence: int
    source_port: str
    source_channel: str
    destination_port: str
    destination_channel: str
    data: bytes
    timeout_height: _client_pb2.Height
    timeout_timestamp: int
    def __init__(self, sequence: _Optional[int] = ..., source_port: _Optional[str] = ..., source_channel: _Optional[str] = ..., destination_port: _Optional[str] = ..., destination_channel: _Optional[str] = ..., data: _Optional[bytes] = ..., timeout_height: _Optional[_Union[_client_pb2.Height, _Mapping]] = ..., timeout_timestamp: _Optional[int] = ...) -> None: ...

class PacketState(_message.Message):
    __slots__ = ["port_id", "channel_id", "sequence", "data"]
    PORT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    port_id: str
    channel_id: str
    sequence: int
    data: bytes
    def __init__(self, port_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., sequence: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class PacketId(_message.Message):
    __slots__ = ["port_id", "channel_id", "sequence"]
    PORT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    port_id: str
    channel_id: str
    sequence: int
    def __init__(self, port_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., sequence: _Optional[int] = ...) -> None: ...

class Acknowledgement(_message.Message):
    __slots__ = ["result", "error"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    result: bytes
    error: str
    def __init__(self, result: _Optional[bytes] = ..., error: _Optional[str] = ...) -> None: ...
