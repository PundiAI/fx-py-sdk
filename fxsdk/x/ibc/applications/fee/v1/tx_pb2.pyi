from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from fxsdk.x.ibc.applications.fee.v1 import fee_pb2 as _fee_pb2
from fxsdk.x.ibc.core.channel.v1 import channel_pb2 as _channel_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MsgRegisterPayee(_message.Message):
    __slots__ = ["port_id", "channel_id", "relayer", "payee"]
    PORT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    RELAYER_FIELD_NUMBER: _ClassVar[int]
    PAYEE_FIELD_NUMBER: _ClassVar[int]
    port_id: str
    channel_id: str
    relayer: str
    payee: str
    def __init__(self, port_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., relayer: _Optional[str] = ..., payee: _Optional[str] = ...) -> None: ...

class MsgRegisterPayeeResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgRegisterCounterpartyPayee(_message.Message):
    __slots__ = ["port_id", "channel_id", "relayer", "counterparty_payee"]
    PORT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    RELAYER_FIELD_NUMBER: _ClassVar[int]
    COUNTERPARTY_PAYEE_FIELD_NUMBER: _ClassVar[int]
    port_id: str
    channel_id: str
    relayer: str
    counterparty_payee: str
    def __init__(self, port_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., relayer: _Optional[str] = ..., counterparty_payee: _Optional[str] = ...) -> None: ...

class MsgRegisterCounterpartyPayeeResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgPayPacketFee(_message.Message):
    __slots__ = ["fee", "source_port_id", "source_channel_id", "signer", "relayers"]
    FEE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PORT_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNER_FIELD_NUMBER: _ClassVar[int]
    RELAYERS_FIELD_NUMBER: _ClassVar[int]
    fee: _fee_pb2.Fee
    source_port_id: str
    source_channel_id: str
    signer: str
    relayers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, fee: _Optional[_Union[_fee_pb2.Fee, _Mapping]] = ..., source_port_id: _Optional[str] = ..., source_channel_id: _Optional[str] = ..., signer: _Optional[str] = ..., relayers: _Optional[_Iterable[str]] = ...) -> None: ...

class MsgPayPacketFeeResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgPayPacketFeeAsync(_message.Message):
    __slots__ = ["packet_id", "packet_fee"]
    PACKET_ID_FIELD_NUMBER: _ClassVar[int]
    PACKET_FEE_FIELD_NUMBER: _ClassVar[int]
    packet_id: _channel_pb2.PacketId
    packet_fee: _fee_pb2.PacketFee
    def __init__(self, packet_id: _Optional[_Union[_channel_pb2.PacketId, _Mapping]] = ..., packet_fee: _Optional[_Union[_fee_pb2.PacketFee, _Mapping]] = ...) -> None: ...

class MsgPayPacketFeeAsyncResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
