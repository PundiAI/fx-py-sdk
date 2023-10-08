from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NetAddress(_message.Message):
    __slots__ = ["id", "ip", "port"]
    ID_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    ip: str
    port: int
    def __init__(self, id: _Optional[str] = ..., ip: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class ProtocolVersion(_message.Message):
    __slots__ = ["p2p", "block", "app"]
    P2P_FIELD_NUMBER: _ClassVar[int]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    APP_FIELD_NUMBER: _ClassVar[int]
    p2p: int
    block: int
    app: int
    def __init__(self, p2p: _Optional[int] = ..., block: _Optional[int] = ..., app: _Optional[int] = ...) -> None: ...

class DefaultNodeInfo(_message.Message):
    __slots__ = ["protocol_version", "default_node_id", "listen_addr", "network", "version", "channels", "moniker", "other"]
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    LISTEN_ADDR_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    MONIKER_FIELD_NUMBER: _ClassVar[int]
    OTHER_FIELD_NUMBER: _ClassVar[int]
    protocol_version: ProtocolVersion
    default_node_id: str
    listen_addr: str
    network: str
    version: str
    channels: bytes
    moniker: str
    other: DefaultNodeInfoOther
    def __init__(self, protocol_version: _Optional[_Union[ProtocolVersion, _Mapping]] = ..., default_node_id: _Optional[str] = ..., listen_addr: _Optional[str] = ..., network: _Optional[str] = ..., version: _Optional[str] = ..., channels: _Optional[bytes] = ..., moniker: _Optional[str] = ..., other: _Optional[_Union[DefaultNodeInfoOther, _Mapping]] = ...) -> None: ...

class DefaultNodeInfoOther(_message.Message):
    __slots__ = ["tx_index", "rpc_address"]
    TX_INDEX_FIELD_NUMBER: _ClassVar[int]
    RPC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    tx_index: str
    rpc_address: str
    def __init__(self, tx_index: _Optional[str] = ..., rpc_address: _Optional[str] = ...) -> None: ...
