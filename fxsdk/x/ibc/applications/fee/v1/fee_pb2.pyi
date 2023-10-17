from fxsdk.x.cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from fxsdk.x.ibc.core.channel.v1 import channel_pb2 as _channel_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Fee(_message.Message):
    __slots__ = ["recv_fee", "ack_fee", "timeout_fee"]
    RECV_FEE_FIELD_NUMBER: _ClassVar[int]
    ACK_FEE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FEE_FIELD_NUMBER: _ClassVar[int]
    recv_fee: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    ack_fee: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    timeout_fee: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    def __init__(self, recv_fee: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ..., ack_fee: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ..., timeout_fee: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ...) -> None: ...

class PacketFee(_message.Message):
    __slots__ = ["fee", "refund_address", "relayers"]
    FEE_FIELD_NUMBER: _ClassVar[int]
    REFUND_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    RELAYERS_FIELD_NUMBER: _ClassVar[int]
    fee: Fee
    refund_address: str
    relayers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, fee: _Optional[_Union[Fee, _Mapping]] = ..., refund_address: _Optional[str] = ..., relayers: _Optional[_Iterable[str]] = ...) -> None: ...

class PacketFees(_message.Message):
    __slots__ = ["packet_fees"]
    PACKET_FEES_FIELD_NUMBER: _ClassVar[int]
    packet_fees: _containers.RepeatedCompositeFieldContainer[PacketFee]
    def __init__(self, packet_fees: _Optional[_Iterable[_Union[PacketFee, _Mapping]]] = ...) -> None: ...

class IdentifiedPacketFees(_message.Message):
    __slots__ = ["packet_id", "packet_fees"]
    PACKET_ID_FIELD_NUMBER: _ClassVar[int]
    PACKET_FEES_FIELD_NUMBER: _ClassVar[int]
    packet_id: _channel_pb2.PacketId
    packet_fees: _containers.RepeatedCompositeFieldContainer[PacketFee]
    def __init__(self, packet_id: _Optional[_Union[_channel_pb2.PacketId, _Mapping]] = ..., packet_fees: _Optional[_Iterable[_Union[PacketFee, _Mapping]]] = ...) -> None: ...
