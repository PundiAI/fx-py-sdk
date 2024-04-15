from fxsdk.x.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BaseAccount(_message.Message):
    __slots__ = ["address", "pub_key", "account_number", "sequence"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    address: str
    pub_key: _any_pb2.Any
    account_number: int
    sequence: int
    def __init__(self, address: _Optional[str] = ..., pub_key: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., account_number: _Optional[int] = ..., sequence: _Optional[int] = ...) -> None: ...

class ModuleAccount(_message.Message):
    __slots__ = ["base_account", "name", "permissions"]
    BASE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    base_account: BaseAccount
    name: str
    permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, base_account: _Optional[_Union[BaseAccount, _Mapping]] = ..., name: _Optional[str] = ..., permissions: _Optional[_Iterable[str]] = ...) -> None: ...

class Params(_message.Message):
    __slots__ = ["max_memo_characters", "tx_sig_limit", "tx_size_cost_per_byte", "sig_verify_cost_ed25519", "sig_verify_cost_secp256k1"]
    MAX_MEMO_CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    TX_SIG_LIMIT_FIELD_NUMBER: _ClassVar[int]
    TX_SIZE_COST_PER_BYTE_FIELD_NUMBER: _ClassVar[int]
    SIG_VERIFY_COST_ED25519_FIELD_NUMBER: _ClassVar[int]
    SIG_VERIFY_COST_SECP256K1_FIELD_NUMBER: _ClassVar[int]
    max_memo_characters: int
    tx_sig_limit: int
    tx_size_cost_per_byte: int
    sig_verify_cost_ed25519: int
    sig_verify_cost_secp256k1: int
    def __init__(self, max_memo_characters: _Optional[int] = ..., tx_sig_limit: _Optional[int] = ..., tx_size_cost_per_byte: _Optional[int] = ..., sig_verify_cost_ed25519: _Optional[int] = ..., sig_verify_cost_secp256k1: _Optional[int] = ...) -> None: ...
