from gogoproto import gogo_pb2 as _gogo_pb2
from ibc.applications.interchain_accounts.v1 import packet_pb2 as _packet_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MsgRegisterInterchainAccount(_message.Message):
    __slots__ = ["owner", "connection_id", "version"]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    owner: str
    connection_id: str
    version: str
    def __init__(self, owner: _Optional[str] = ..., connection_id: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class MsgRegisterInterchainAccountResponse(_message.Message):
    __slots__ = ["channel_id"]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    def __init__(self, channel_id: _Optional[str] = ...) -> None: ...

class MsgSendTx(_message.Message):
    __slots__ = ["owner", "connection_id", "packet_data", "relative_timeout"]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    PACKET_DATA_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    owner: str
    connection_id: str
    packet_data: _packet_pb2.InterchainAccountPacketData
    relative_timeout: int
    def __init__(self, owner: _Optional[str] = ..., connection_id: _Optional[str] = ..., packet_data: _Optional[_Union[_packet_pb2.InterchainAccountPacketData, _Mapping]] = ..., relative_timeout: _Optional[int] = ...) -> None: ...

class MsgSendTxResponse(_message.Message):
    __slots__ = ["sequence"]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    sequence: int
    def __init__(self, sequence: _Optional[int] = ...) -> None: ...
