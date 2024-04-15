from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from fxpysdk.fxsdk.x.ibc.applications.fee.v1 import fee_pb2 as _fee_pb2
from fxpysdk.fxsdk.x.ibc.core.channel.v1 import channel_pb2 as _channel_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ["identified_fees", "fee_enabled_channels", "registered_payees", "registered_counterparty_payees", "forward_relayers"]
    IDENTIFIED_FEES_FIELD_NUMBER: _ClassVar[int]
    FEE_ENABLED_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_PAYEES_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_COUNTERPARTY_PAYEES_FIELD_NUMBER: _ClassVar[int]
    FORWARD_RELAYERS_FIELD_NUMBER: _ClassVar[int]
    identified_fees: _containers.RepeatedCompositeFieldContainer[_fee_pb2.IdentifiedPacketFees]
    fee_enabled_channels: _containers.RepeatedCompositeFieldContainer[FeeEnabledChannel]
    registered_payees: _containers.RepeatedCompositeFieldContainer[RegisteredPayee]
    registered_counterparty_payees: _containers.RepeatedCompositeFieldContainer[RegisteredCounterpartyPayee]
    forward_relayers: _containers.RepeatedCompositeFieldContainer[ForwardRelayerAddress]
    def __init__(self, identified_fees: _Optional[_Iterable[_Union[_fee_pb2.IdentifiedPacketFees, _Mapping]]] = ..., fee_enabled_channels: _Optional[_Iterable[_Union[FeeEnabledChannel, _Mapping]]] = ..., registered_payees: _Optional[_Iterable[_Union[RegisteredPayee, _Mapping]]] = ..., registered_counterparty_payees: _Optional[_Iterable[_Union[RegisteredCounterpartyPayee, _Mapping]]] = ..., forward_relayers: _Optional[_Iterable[_Union[ForwardRelayerAddress, _Mapping]]] = ...) -> None: ...

class FeeEnabledChannel(_message.Message):
    __slots__ = ["port_id", "channel_id"]
    PORT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    port_id: str
    channel_id: str
    def __init__(self, port_id: _Optional[str] = ..., channel_id: _Optional[str] = ...) -> None: ...

class RegisteredPayee(_message.Message):
    __slots__ = ["channel_id", "relayer", "payee"]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    RELAYER_FIELD_NUMBER: _ClassVar[int]
    PAYEE_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    relayer: str
    payee: str
    def __init__(self, channel_id: _Optional[str] = ..., relayer: _Optional[str] = ..., payee: _Optional[str] = ...) -> None: ...

class RegisteredCounterpartyPayee(_message.Message):
    __slots__ = ["channel_id", "relayer", "counterparty_payee"]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    RELAYER_FIELD_NUMBER: _ClassVar[int]
    COUNTERPARTY_PAYEE_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    relayer: str
    counterparty_payee: str
    def __init__(self, channel_id: _Optional[str] = ..., relayer: _Optional[str] = ..., counterparty_payee: _Optional[str] = ...) -> None: ...

class ForwardRelayerAddress(_message.Message):
    __slots__ = ["address", "packet_id"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PACKET_ID_FIELD_NUMBER: _ClassVar[int]
    address: str
    packet_id: _channel_pb2.PacketId
    def __init__(self, address: _Optional[str] = ..., packet_id: _Optional[_Union[_channel_pb2.PacketId, _Mapping]] = ...) -> None: ...
