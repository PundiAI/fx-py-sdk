from gogoproto import gogo_pb2 as _gogo_pb2
from google.api import annotations_pb2 as _annotations_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as _pagination_pb2
from ibc.applications.fee.v1 import fee_pb2 as _fee_pb2
from ibc.applications.fee.v1 import genesis_pb2 as _genesis_pb2
from ibc.core.channel.v1 import channel_pb2 as _channel_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryIncentivizedPacketsRequest(_message.Message):
    __slots__ = ["pagination", "query_height"]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    QUERY_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.PageRequest
    query_height: int
    def __init__(self, pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ..., query_height: _Optional[int] = ...) -> None: ...

class QueryIncentivizedPacketsResponse(_message.Message):
    __slots__ = ["incentivized_packets"]
    INCENTIVIZED_PACKETS_FIELD_NUMBER: _ClassVar[int]
    incentivized_packets: _containers.RepeatedCompositeFieldContainer[_fee_pb2.IdentifiedPacketFees]
    def __init__(self, incentivized_packets: _Optional[_Iterable[_Union[_fee_pb2.IdentifiedPacketFees, _Mapping]]] = ...) -> None: ...

class QueryIncentivizedPacketRequest(_message.Message):
    __slots__ = ["packet_id", "query_height"]
    PACKET_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    packet_id: _channel_pb2.PacketId
    query_height: int
    def __init__(self, packet_id: _Optional[_Union[_channel_pb2.PacketId, _Mapping]] = ..., query_height: _Optional[int] = ...) -> None: ...

class QueryIncentivizedPacketResponse(_message.Message):
    __slots__ = ["incentivized_packet"]
    INCENTIVIZED_PACKET_FIELD_NUMBER: _ClassVar[int]
    incentivized_packet: _fee_pb2.IdentifiedPacketFees
    def __init__(self, incentivized_packet: _Optional[_Union[_fee_pb2.IdentifiedPacketFees, _Mapping]] = ...) -> None: ...

class QueryIncentivizedPacketsForChannelRequest(_message.Message):
    __slots__ = ["pagination", "port_id", "channel_id", "query_height"]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    PORT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.PageRequest
    port_id: str
    channel_id: str
    query_height: int
    def __init__(self, pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ..., port_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., query_height: _Optional[int] = ...) -> None: ...

class QueryIncentivizedPacketsForChannelResponse(_message.Message):
    __slots__ = ["incentivized_packets"]
    INCENTIVIZED_PACKETS_FIELD_NUMBER: _ClassVar[int]
    incentivized_packets: _containers.RepeatedCompositeFieldContainer[_fee_pb2.IdentifiedPacketFees]
    def __init__(self, incentivized_packets: _Optional[_Iterable[_Union[_fee_pb2.IdentifiedPacketFees, _Mapping]]] = ...) -> None: ...

class QueryTotalRecvFeesRequest(_message.Message):
    __slots__ = ["packet_id"]
    PACKET_ID_FIELD_NUMBER: _ClassVar[int]
    packet_id: _channel_pb2.PacketId
    def __init__(self, packet_id: _Optional[_Union[_channel_pb2.PacketId, _Mapping]] = ...) -> None: ...

class QueryTotalRecvFeesResponse(_message.Message):
    __slots__ = ["recv_fees"]
    RECV_FEES_FIELD_NUMBER: _ClassVar[int]
    recv_fees: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    def __init__(self, recv_fees: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ...) -> None: ...

class QueryTotalAckFeesRequest(_message.Message):
    __slots__ = ["packet_id"]
    PACKET_ID_FIELD_NUMBER: _ClassVar[int]
    packet_id: _channel_pb2.PacketId
    def __init__(self, packet_id: _Optional[_Union[_channel_pb2.PacketId, _Mapping]] = ...) -> None: ...

class QueryTotalAckFeesResponse(_message.Message):
    __slots__ = ["ack_fees"]
    ACK_FEES_FIELD_NUMBER: _ClassVar[int]
    ack_fees: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    def __init__(self, ack_fees: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ...) -> None: ...

class QueryTotalTimeoutFeesRequest(_message.Message):
    __slots__ = ["packet_id"]
    PACKET_ID_FIELD_NUMBER: _ClassVar[int]
    packet_id: _channel_pb2.PacketId
    def __init__(self, packet_id: _Optional[_Union[_channel_pb2.PacketId, _Mapping]] = ...) -> None: ...

class QueryTotalTimeoutFeesResponse(_message.Message):
    __slots__ = ["timeout_fees"]
    TIMEOUT_FEES_FIELD_NUMBER: _ClassVar[int]
    timeout_fees: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    def __init__(self, timeout_fees: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ...) -> None: ...

class QueryPayeeRequest(_message.Message):
    __slots__ = ["channel_id", "relayer"]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    RELAYER_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    relayer: str
    def __init__(self, channel_id: _Optional[str] = ..., relayer: _Optional[str] = ...) -> None: ...

class QueryPayeeResponse(_message.Message):
    __slots__ = ["payee_address"]
    PAYEE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    payee_address: str
    def __init__(self, payee_address: _Optional[str] = ...) -> None: ...

class QueryCounterpartyPayeeRequest(_message.Message):
    __slots__ = ["channel_id", "relayer"]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    RELAYER_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    relayer: str
    def __init__(self, channel_id: _Optional[str] = ..., relayer: _Optional[str] = ...) -> None: ...

class QueryCounterpartyPayeeResponse(_message.Message):
    __slots__ = ["counterparty_payee"]
    COUNTERPARTY_PAYEE_FIELD_NUMBER: _ClassVar[int]
    counterparty_payee: str
    def __init__(self, counterparty_payee: _Optional[str] = ...) -> None: ...

class QueryFeeEnabledChannelsRequest(_message.Message):
    __slots__ = ["pagination", "query_height"]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    QUERY_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.PageRequest
    query_height: int
    def __init__(self, pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ..., query_height: _Optional[int] = ...) -> None: ...

class QueryFeeEnabledChannelsResponse(_message.Message):
    __slots__ = ["fee_enabled_channels"]
    FEE_ENABLED_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    fee_enabled_channels: _containers.RepeatedCompositeFieldContainer[_genesis_pb2.FeeEnabledChannel]
    def __init__(self, fee_enabled_channels: _Optional[_Iterable[_Union[_genesis_pb2.FeeEnabledChannel, _Mapping]]] = ...) -> None: ...

class QueryFeeEnabledChannelRequest(_message.Message):
    __slots__ = ["port_id", "channel_id"]
    PORT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    port_id: str
    channel_id: str
    def __init__(self, port_id: _Optional[str] = ..., channel_id: _Optional[str] = ...) -> None: ...

class QueryFeeEnabledChannelResponse(_message.Message):
    __slots__ = ["fee_enabled"]
    FEE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    fee_enabled: bool
    def __init__(self, fee_enabled: bool = ...) -> None: ...
