from ibc.core.connection.v1 import connection_pb2 as _connection_pb2
from ibc.core.channel.v1 import channel_pb2 as _channel_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DATA_TYPE_UNINITIALIZED_UNSPECIFIED: _ClassVar[DataType]
    DATA_TYPE_CLIENT_STATE: _ClassVar[DataType]
    DATA_TYPE_CONSENSUS_STATE: _ClassVar[DataType]
    DATA_TYPE_CONNECTION_STATE: _ClassVar[DataType]
    DATA_TYPE_CHANNEL_STATE: _ClassVar[DataType]
    DATA_TYPE_PACKET_COMMITMENT: _ClassVar[DataType]
    DATA_TYPE_PACKET_ACKNOWLEDGEMENT: _ClassVar[DataType]
    DATA_TYPE_PACKET_RECEIPT_ABSENCE: _ClassVar[DataType]
    DATA_TYPE_NEXT_SEQUENCE_RECV: _ClassVar[DataType]
    DATA_TYPE_HEADER: _ClassVar[DataType]
DATA_TYPE_UNINITIALIZED_UNSPECIFIED: DataType
DATA_TYPE_CLIENT_STATE: DataType
DATA_TYPE_CONSENSUS_STATE: DataType
DATA_TYPE_CONNECTION_STATE: DataType
DATA_TYPE_CHANNEL_STATE: DataType
DATA_TYPE_PACKET_COMMITMENT: DataType
DATA_TYPE_PACKET_ACKNOWLEDGEMENT: DataType
DATA_TYPE_PACKET_RECEIPT_ABSENCE: DataType
DATA_TYPE_NEXT_SEQUENCE_RECV: DataType
DATA_TYPE_HEADER: DataType

class ClientState(_message.Message):
    __slots__ = ["sequence", "frozen_sequence", "consensus_state", "allow_update_after_proposal"]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    FROZEN_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    CONSENSUS_STATE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_UPDATE_AFTER_PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    sequence: int
    frozen_sequence: int
    consensus_state: ConsensusState
    allow_update_after_proposal: bool
    def __init__(self, sequence: _Optional[int] = ..., frozen_sequence: _Optional[int] = ..., consensus_state: _Optional[_Union[ConsensusState, _Mapping]] = ..., allow_update_after_proposal: bool = ...) -> None: ...

class ConsensusState(_message.Message):
    __slots__ = ["public_key", "diversifier", "timestamp"]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    DIVERSIFIER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    public_key: _any_pb2.Any
    diversifier: str
    timestamp: int
    def __init__(self, public_key: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., diversifier: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...

class Header(_message.Message):
    __slots__ = ["sequence", "timestamp", "signature", "new_public_key", "new_diversifier"]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    NEW_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    NEW_DIVERSIFIER_FIELD_NUMBER: _ClassVar[int]
    sequence: int
    timestamp: int
    signature: bytes
    new_public_key: _any_pb2.Any
    new_diversifier: str
    def __init__(self, sequence: _Optional[int] = ..., timestamp: _Optional[int] = ..., signature: _Optional[bytes] = ..., new_public_key: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., new_diversifier: _Optional[str] = ...) -> None: ...

class Misbehaviour(_message.Message):
    __slots__ = ["client_id", "sequence", "signature_one", "signature_two"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_ONE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_TWO_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    sequence: int
    signature_one: SignatureAndData
    signature_two: SignatureAndData
    def __init__(self, client_id: _Optional[str] = ..., sequence: _Optional[int] = ..., signature_one: _Optional[_Union[SignatureAndData, _Mapping]] = ..., signature_two: _Optional[_Union[SignatureAndData, _Mapping]] = ...) -> None: ...

class SignatureAndData(_message.Message):
    __slots__ = ["signature", "data_type", "data", "timestamp"]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    signature: bytes
    data_type: DataType
    data: bytes
    timestamp: int
    def __init__(self, signature: _Optional[bytes] = ..., data_type: _Optional[_Union[DataType, str]] = ..., data: _Optional[bytes] = ..., timestamp: _Optional[int] = ...) -> None: ...

class TimestampedSignatureData(_message.Message):
    __slots__ = ["signature_data", "timestamp"]
    SIGNATURE_DATA_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    signature_data: bytes
    timestamp: int
    def __init__(self, signature_data: _Optional[bytes] = ..., timestamp: _Optional[int] = ...) -> None: ...

class SignBytes(_message.Message):
    __slots__ = ["sequence", "timestamp", "diversifier", "data_type", "data"]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DIVERSIFIER_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    sequence: int
    timestamp: int
    diversifier: str
    data_type: DataType
    data: bytes
    def __init__(self, sequence: _Optional[int] = ..., timestamp: _Optional[int] = ..., diversifier: _Optional[str] = ..., data_type: _Optional[_Union[DataType, str]] = ..., data: _Optional[bytes] = ...) -> None: ...

class HeaderData(_message.Message):
    __slots__ = ["new_pub_key", "new_diversifier"]
    NEW_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    NEW_DIVERSIFIER_FIELD_NUMBER: _ClassVar[int]
    new_pub_key: _any_pb2.Any
    new_diversifier: str
    def __init__(self, new_pub_key: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., new_diversifier: _Optional[str] = ...) -> None: ...

class ClientStateData(_message.Message):
    __slots__ = ["path", "client_state"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    CLIENT_STATE_FIELD_NUMBER: _ClassVar[int]
    path: bytes
    client_state: _any_pb2.Any
    def __init__(self, path: _Optional[bytes] = ..., client_state: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class ConsensusStateData(_message.Message):
    __slots__ = ["path", "consensus_state"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    CONSENSUS_STATE_FIELD_NUMBER: _ClassVar[int]
    path: bytes
    consensus_state: _any_pb2.Any
    def __init__(self, path: _Optional[bytes] = ..., consensus_state: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class ConnectionStateData(_message.Message):
    __slots__ = ["path", "connection"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    path: bytes
    connection: _connection_pb2.ConnectionEnd
    def __init__(self, path: _Optional[bytes] = ..., connection: _Optional[_Union[_connection_pb2.ConnectionEnd, _Mapping]] = ...) -> None: ...

class ChannelStateData(_message.Message):
    __slots__ = ["path", "channel"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    path: bytes
    channel: _channel_pb2.Channel
    def __init__(self, path: _Optional[bytes] = ..., channel: _Optional[_Union[_channel_pb2.Channel, _Mapping]] = ...) -> None: ...

class PacketCommitmentData(_message.Message):
    __slots__ = ["path", "commitment"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    COMMITMENT_FIELD_NUMBER: _ClassVar[int]
    path: bytes
    commitment: bytes
    def __init__(self, path: _Optional[bytes] = ..., commitment: _Optional[bytes] = ...) -> None: ...

class PacketAcknowledgementData(_message.Message):
    __slots__ = ["path", "acknowledgement"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEMENT_FIELD_NUMBER: _ClassVar[int]
    path: bytes
    acknowledgement: bytes
    def __init__(self, path: _Optional[bytes] = ..., acknowledgement: _Optional[bytes] = ...) -> None: ...

class PacketReceiptAbsenceData(_message.Message):
    __slots__ = ["path"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: bytes
    def __init__(self, path: _Optional[bytes] = ...) -> None: ...

class NextSequenceRecvData(_message.Message):
    __slots__ = ["path", "next_seq_recv"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    NEXT_SEQ_RECV_FIELD_NUMBER: _ClassVar[int]
    path: bytes
    next_seq_recv: int
    def __init__(self, path: _Optional[bytes] = ..., next_seq_recv: _Optional[int] = ...) -> None: ...
