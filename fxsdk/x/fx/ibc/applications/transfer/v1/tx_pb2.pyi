from fxpysdk.fxsdk.x.cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from fxpysdk.fxsdk.x.ibc.applications.transfer.v1 import tx_pb2 as _tx_pb2
from fxpysdk.fxsdk.x.ibc.core.client.v1 import client_pb2 as _client_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MsgTransfer(_message.Message):
    __slots__ = ["source_port", "source_channel", "token", "sender", "receiver", "timeout_height", "timeout_timestamp", "router", "fee", "memo"]
    SOURCE_PORT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ROUTER_FIELD_NUMBER: _ClassVar[int]
    FEE_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    source_port: str
    source_channel: str
    token: _coin_pb2.Coin
    sender: str
    receiver: str
    timeout_height: _client_pb2.Height
    timeout_timestamp: int
    router: str
    fee: _coin_pb2.Coin
    memo: str
    def __init__(self, source_port: _Optional[str] = ..., source_channel: _Optional[str] = ..., token: _Optional[_Union[_coin_pb2.Coin, _Mapping]] = ..., sender: _Optional[str] = ..., receiver: _Optional[str] = ..., timeout_height: _Optional[_Union[_client_pb2.Height, _Mapping]] = ..., timeout_timestamp: _Optional[int] = ..., router: _Optional[str] = ..., fee: _Optional[_Union[_coin_pb2.Coin, _Mapping]] = ..., memo: _Optional[str] = ...) -> None: ...
