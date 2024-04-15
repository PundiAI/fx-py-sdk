from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from fxpysdk.fxsdk.x.ibc.core.client.v1 import client_pb2 as _client_pb2
from fxpysdk.fxsdk.x.ibc.core.channel.v1 import channel_pb2 as _channel_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResponseResultType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    RESPONSE_RESULT_TYPE_UNSPECIFIED: _ClassVar[ResponseResultType]
    RESPONSE_RESULT_TYPE_NOOP: _ClassVar[ResponseResultType]
    RESPONSE_RESULT_TYPE_SUCCESS: _ClassVar[ResponseResultType]
RESPONSE_RESULT_TYPE_UNSPECIFIED: ResponseResultType
RESPONSE_RESULT_TYPE_NOOP: ResponseResultType
RESPONSE_RESULT_TYPE_SUCCESS: ResponseResultType

class MsgChannelOpenInit(_message.Message):
    __slots__ = ["port_id", "channel", "signer"]
    PORT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    SIGNER_FIELD_NUMBER: _ClassVar[int]
    port_id: str
    channel: _channel_pb2.Channel
    signer: str
    def __init__(self, port_id: _Optional[str] = ..., channel: _Optional[_Union[_channel_pb2.Channel, _Mapping]] = ..., signer: _Optional[str] = ...) -> None: ...

class MsgChannelOpenInitResponse(_message.Message):
    __slots__ = ["channel_id", "version"]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    version: str
    def __init__(self, channel_id: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class MsgChannelOpenTry(_message.Message):
    __slots__ = ["port_id", "previous_channel_id", "channel", "counterparty_version", "proof_init", "proof_height", "signer"]
    PORT_ID_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    COUNTERPARTY_VERSION_FIELD_NUMBER: _ClassVar[int]
    PROOF_INIT_FIELD_NUMBER: _ClassVar[int]
    PROOF_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    SIGNER_FIELD_NUMBER: _ClassVar[int]
    port_id: str
    previous_channel_id: str
    channel: _channel_pb2.Channel
    counterparty_version: str
    proof_init: bytes
    proof_height: _client_pb2.Height
    signer: str
    def __init__(self, port_id: _Optional[str] = ..., previous_channel_id: _Optional[str] = ..., channel: _Optional[_Union[_channel_pb2.Channel, _Mapping]] = ..., counterparty_version: _Optional[str] = ..., proof_init: _Optional[bytes] = ..., proof_height: _Optional[_Union[_client_pb2.Height, _Mapping]] = ..., signer: _Optional[str] = ...) -> None: ...

class MsgChannelOpenTryResponse(_message.Message):
    __slots__ = ["version"]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: str
    def __init__(self, version: _Optional[str] = ...) -> None: ...

class MsgChannelOpenAck(_message.Message):
    __slots__ = ["port_id", "channel_id", "counterparty_channel_id", "counterparty_version", "proof_try", "proof_height", "signer"]
    PORT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    COUNTERPARTY_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    COUNTERPARTY_VERSION_FIELD_NUMBER: _ClassVar[int]
    PROOF_TRY_FIELD_NUMBER: _ClassVar[int]
    PROOF_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    SIGNER_FIELD_NUMBER: _ClassVar[int]
    port_id: str
    channel_id: str
    counterparty_channel_id: str
    counterparty_version: str
    proof_try: bytes
    proof_height: _client_pb2.Height
    signer: str
    def __init__(self, port_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., counterparty_channel_id: _Optional[str] = ..., counterparty_version: _Optional[str] = ..., proof_try: _Optional[bytes] = ..., proof_height: _Optional[_Union[_client_pb2.Height, _Mapping]] = ..., signer: _Optional[str] = ...) -> None: ...

class MsgChannelOpenAckResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgChannelOpenConfirm(_message.Message):
    __slots__ = ["port_id", "channel_id", "proof_ack", "proof_height", "signer"]
    PORT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    PROOF_ACK_FIELD_NUMBER: _ClassVar[int]
    PROOF_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    SIGNER_FIELD_NUMBER: _ClassVar[int]
    port_id: str
    channel_id: str
    proof_ack: bytes
    proof_height: _client_pb2.Height
    signer: str
    def __init__(self, port_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., proof_ack: _Optional[bytes] = ..., proof_height: _Optional[_Union[_client_pb2.Height, _Mapping]] = ..., signer: _Optional[str] = ...) -> None: ...

class MsgChannelOpenConfirmResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgChannelCloseInit(_message.Message):
    __slots__ = ["port_id", "channel_id", "signer"]
    PORT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNER_FIELD_NUMBER: _ClassVar[int]
    port_id: str
    channel_id: str
    signer: str
    def __init__(self, port_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., signer: _Optional[str] = ...) -> None: ...

class MsgChannelCloseInitResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgChannelCloseConfirm(_message.Message):
    __slots__ = ["port_id", "channel_id", "proof_init", "proof_height", "signer"]
    PORT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    PROOF_INIT_FIELD_NUMBER: _ClassVar[int]
    PROOF_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    SIGNER_FIELD_NUMBER: _ClassVar[int]
    port_id: str
    channel_id: str
    proof_init: bytes
    proof_height: _client_pb2.Height
    signer: str
    def __init__(self, port_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., proof_init: _Optional[bytes] = ..., proof_height: _Optional[_Union[_client_pb2.Height, _Mapping]] = ..., signer: _Optional[str] = ...) -> None: ...

class MsgChannelCloseConfirmResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgRecvPacket(_message.Message):
    __slots__ = ["packet", "proof_commitment", "proof_height", "signer"]
    PACKET_FIELD_NUMBER: _ClassVar[int]
    PROOF_COMMITMENT_FIELD_NUMBER: _ClassVar[int]
    PROOF_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    SIGNER_FIELD_NUMBER: _ClassVar[int]
    packet: _channel_pb2.Packet
    proof_commitment: bytes
    proof_height: _client_pb2.Height
    signer: str
    def __init__(self, packet: _Optional[_Union[_channel_pb2.Packet, _Mapping]] = ..., proof_commitment: _Optional[bytes] = ..., proof_height: _Optional[_Union[_client_pb2.Height, _Mapping]] = ..., signer: _Optional[str] = ...) -> None: ...

class MsgRecvPacketResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: ResponseResultType
    def __init__(self, result: _Optional[_Union[ResponseResultType, str]] = ...) -> None: ...

class MsgTimeout(_message.Message):
    __slots__ = ["packet", "proof_unreceived", "proof_height", "next_sequence_recv", "signer"]
    PACKET_FIELD_NUMBER: _ClassVar[int]
    PROOF_UNRECEIVED_FIELD_NUMBER: _ClassVar[int]
    PROOF_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    NEXT_SEQUENCE_RECV_FIELD_NUMBER: _ClassVar[int]
    SIGNER_FIELD_NUMBER: _ClassVar[int]
    packet: _channel_pb2.Packet
    proof_unreceived: bytes
    proof_height: _client_pb2.Height
    next_sequence_recv: int
    signer: str
    def __init__(self, packet: _Optional[_Union[_channel_pb2.Packet, _Mapping]] = ..., proof_unreceived: _Optional[bytes] = ..., proof_height: _Optional[_Union[_client_pb2.Height, _Mapping]] = ..., next_sequence_recv: _Optional[int] = ..., signer: _Optional[str] = ...) -> None: ...

class MsgTimeoutResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: ResponseResultType
    def __init__(self, result: _Optional[_Union[ResponseResultType, str]] = ...) -> None: ...

class MsgTimeoutOnClose(_message.Message):
    __slots__ = ["packet", "proof_unreceived", "proof_close", "proof_height", "next_sequence_recv", "signer"]
    PACKET_FIELD_NUMBER: _ClassVar[int]
    PROOF_UNRECEIVED_FIELD_NUMBER: _ClassVar[int]
    PROOF_CLOSE_FIELD_NUMBER: _ClassVar[int]
    PROOF_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    NEXT_SEQUENCE_RECV_FIELD_NUMBER: _ClassVar[int]
    SIGNER_FIELD_NUMBER: _ClassVar[int]
    packet: _channel_pb2.Packet
    proof_unreceived: bytes
    proof_close: bytes
    proof_height: _client_pb2.Height
    next_sequence_recv: int
    signer: str
    def __init__(self, packet: _Optional[_Union[_channel_pb2.Packet, _Mapping]] = ..., proof_unreceived: _Optional[bytes] = ..., proof_close: _Optional[bytes] = ..., proof_height: _Optional[_Union[_client_pb2.Height, _Mapping]] = ..., next_sequence_recv: _Optional[int] = ..., signer: _Optional[str] = ...) -> None: ...

class MsgTimeoutOnCloseResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: ResponseResultType
    def __init__(self, result: _Optional[_Union[ResponseResultType, str]] = ...) -> None: ...

class MsgAcknowledgement(_message.Message):
    __slots__ = ["packet", "acknowledgement", "proof_acked", "proof_height", "signer"]
    PACKET_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEMENT_FIELD_NUMBER: _ClassVar[int]
    PROOF_ACKED_FIELD_NUMBER: _ClassVar[int]
    PROOF_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    SIGNER_FIELD_NUMBER: _ClassVar[int]
    packet: _channel_pb2.Packet
    acknowledgement: bytes
    proof_acked: bytes
    proof_height: _client_pb2.Height
    signer: str
    def __init__(self, packet: _Optional[_Union[_channel_pb2.Packet, _Mapping]] = ..., acknowledgement: _Optional[bytes] = ..., proof_acked: _Optional[bytes] = ..., proof_height: _Optional[_Union[_client_pb2.Height, _Mapping]] = ..., signer: _Optional[str] = ...) -> None: ...

class MsgAcknowledgementResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: ResponseResultType
    def __init__(self, result: _Optional[_Union[ResponseResultType, str]] = ...) -> None: ...
