from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import any_pb2 as _any_pb2
from ibc.core.client.v1 import client_pb2 as _client_pb2
from ibc.core.connection.v1 import connection_pb2 as _connection_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MsgConnectionOpenInit(_message.Message):
    __slots__ = ["client_id", "counterparty", "version", "delay_period", "signer"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    COUNTERPARTY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DELAY_PERIOD_FIELD_NUMBER: _ClassVar[int]
    SIGNER_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    counterparty: _connection_pb2.Counterparty
    version: _connection_pb2.Version
    delay_period: int
    signer: str
    def __init__(self, client_id: _Optional[str] = ..., counterparty: _Optional[_Union[_connection_pb2.Counterparty, _Mapping]] = ..., version: _Optional[_Union[_connection_pb2.Version, _Mapping]] = ..., delay_period: _Optional[int] = ..., signer: _Optional[str] = ...) -> None: ...

class MsgConnectionOpenInitResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgConnectionOpenTry(_message.Message):
    __slots__ = ["client_id", "previous_connection_id", "client_state", "counterparty", "delay_period", "counterparty_versions", "proof_height", "proof_init", "proof_client", "proof_consensus", "consensus_height", "signer"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_STATE_FIELD_NUMBER: _ClassVar[int]
    COUNTERPARTY_FIELD_NUMBER: _ClassVar[int]
    DELAY_PERIOD_FIELD_NUMBER: _ClassVar[int]
    COUNTERPARTY_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    PROOF_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    PROOF_INIT_FIELD_NUMBER: _ClassVar[int]
    PROOF_CLIENT_FIELD_NUMBER: _ClassVar[int]
    PROOF_CONSENSUS_FIELD_NUMBER: _ClassVar[int]
    CONSENSUS_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    SIGNER_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    previous_connection_id: str
    client_state: _any_pb2.Any
    counterparty: _connection_pb2.Counterparty
    delay_period: int
    counterparty_versions: _containers.RepeatedCompositeFieldContainer[_connection_pb2.Version]
    proof_height: _client_pb2.Height
    proof_init: bytes
    proof_client: bytes
    proof_consensus: bytes
    consensus_height: _client_pb2.Height
    signer: str
    def __init__(self, client_id: _Optional[str] = ..., previous_connection_id: _Optional[str] = ..., client_state: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., counterparty: _Optional[_Union[_connection_pb2.Counterparty, _Mapping]] = ..., delay_period: _Optional[int] = ..., counterparty_versions: _Optional[_Iterable[_Union[_connection_pb2.Version, _Mapping]]] = ..., proof_height: _Optional[_Union[_client_pb2.Height, _Mapping]] = ..., proof_init: _Optional[bytes] = ..., proof_client: _Optional[bytes] = ..., proof_consensus: _Optional[bytes] = ..., consensus_height: _Optional[_Union[_client_pb2.Height, _Mapping]] = ..., signer: _Optional[str] = ...) -> None: ...

class MsgConnectionOpenTryResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgConnectionOpenAck(_message.Message):
    __slots__ = ["connection_id", "counterparty_connection_id", "version", "client_state", "proof_height", "proof_try", "proof_client", "proof_consensus", "consensus_height", "signer"]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    COUNTERPARTY_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CLIENT_STATE_FIELD_NUMBER: _ClassVar[int]
    PROOF_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    PROOF_TRY_FIELD_NUMBER: _ClassVar[int]
    PROOF_CLIENT_FIELD_NUMBER: _ClassVar[int]
    PROOF_CONSENSUS_FIELD_NUMBER: _ClassVar[int]
    CONSENSUS_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    SIGNER_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    counterparty_connection_id: str
    version: _connection_pb2.Version
    client_state: _any_pb2.Any
    proof_height: _client_pb2.Height
    proof_try: bytes
    proof_client: bytes
    proof_consensus: bytes
    consensus_height: _client_pb2.Height
    signer: str
    def __init__(self, connection_id: _Optional[str] = ..., counterparty_connection_id: _Optional[str] = ..., version: _Optional[_Union[_connection_pb2.Version, _Mapping]] = ..., client_state: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., proof_height: _Optional[_Union[_client_pb2.Height, _Mapping]] = ..., proof_try: _Optional[bytes] = ..., proof_client: _Optional[bytes] = ..., proof_consensus: _Optional[bytes] = ..., consensus_height: _Optional[_Union[_client_pb2.Height, _Mapping]] = ..., signer: _Optional[str] = ...) -> None: ...

class MsgConnectionOpenAckResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgConnectionOpenConfirm(_message.Message):
    __slots__ = ["connection_id", "proof_ack", "proof_height", "signer"]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    PROOF_ACK_FIELD_NUMBER: _ClassVar[int]
    PROOF_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    SIGNER_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    proof_ack: bytes
    proof_height: _client_pb2.Height
    signer: str
    def __init__(self, connection_id: _Optional[str] = ..., proof_ack: _Optional[bytes] = ..., proof_height: _Optional[_Union[_client_pb2.Height, _Mapping]] = ..., signer: _Optional[str] = ...) -> None: ...

class MsgConnectionOpenConfirmResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
