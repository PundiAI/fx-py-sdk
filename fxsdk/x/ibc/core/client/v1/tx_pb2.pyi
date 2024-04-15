from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MsgCreateClient(_message.Message):
    __slots__ = ["client_state", "consensus_state", "signer"]
    CLIENT_STATE_FIELD_NUMBER: _ClassVar[int]
    CONSENSUS_STATE_FIELD_NUMBER: _ClassVar[int]
    SIGNER_FIELD_NUMBER: _ClassVar[int]
    client_state: _any_pb2.Any
    consensus_state: _any_pb2.Any
    signer: str
    def __init__(self, client_state: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., consensus_state: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., signer: _Optional[str] = ...) -> None: ...

class MsgCreateClientResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgUpdateClient(_message.Message):
    __slots__ = ["client_id", "header", "signer"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SIGNER_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    header: _any_pb2.Any
    signer: str
    def __init__(self, client_id: _Optional[str] = ..., header: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., signer: _Optional[str] = ...) -> None: ...

class MsgUpdateClientResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgUpgradeClient(_message.Message):
    __slots__ = ["client_id", "client_state", "consensus_state", "proof_upgrade_client", "proof_upgrade_consensus_state", "signer"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_STATE_FIELD_NUMBER: _ClassVar[int]
    CONSENSUS_STATE_FIELD_NUMBER: _ClassVar[int]
    PROOF_UPGRADE_CLIENT_FIELD_NUMBER: _ClassVar[int]
    PROOF_UPGRADE_CONSENSUS_STATE_FIELD_NUMBER: _ClassVar[int]
    SIGNER_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    client_state: _any_pb2.Any
    consensus_state: _any_pb2.Any
    proof_upgrade_client: bytes
    proof_upgrade_consensus_state: bytes
    signer: str
    def __init__(self, client_id: _Optional[str] = ..., client_state: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., consensus_state: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., proof_upgrade_client: _Optional[bytes] = ..., proof_upgrade_consensus_state: _Optional[bytes] = ..., signer: _Optional[str] = ...) -> None: ...

class MsgUpgradeClientResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgSubmitMisbehaviour(_message.Message):
    __slots__ = ["client_id", "misbehaviour", "signer"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    MISBEHAVIOUR_FIELD_NUMBER: _ClassVar[int]
    SIGNER_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    misbehaviour: _any_pb2.Any
    signer: str
    def __init__(self, client_id: _Optional[str] = ..., misbehaviour: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., signer: _Optional[str] = ...) -> None: ...

class MsgSubmitMisbehaviourResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
