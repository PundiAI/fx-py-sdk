from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import any_pb2 as _any_pb2
from cosmos.crypto.hd.v1 import hd_pb2 as _hd_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Record(_message.Message):
    __slots__ = ["name", "pub_key", "local", "ledger", "multi", "offline"]
    class Local(_message.Message):
        __slots__ = ["priv_key"]
        PRIV_KEY_FIELD_NUMBER: _ClassVar[int]
        priv_key: _any_pb2.Any
        def __init__(self, priv_key: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
    class Ledger(_message.Message):
        __slots__ = ["path"]
        PATH_FIELD_NUMBER: _ClassVar[int]
        path: _hd_pb2.BIP44Params
        def __init__(self, path: _Optional[_Union[_hd_pb2.BIP44Params, _Mapping]] = ...) -> None: ...
    class Multi(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Offline(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    LOCAL_FIELD_NUMBER: _ClassVar[int]
    LEDGER_FIELD_NUMBER: _ClassVar[int]
    MULTI_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_FIELD_NUMBER: _ClassVar[int]
    name: str
    pub_key: _any_pb2.Any
    local: Record.Local
    ledger: Record.Ledger
    multi: Record.Multi
    offline: Record.Offline
    def __init__(self, name: _Optional[str] = ..., pub_key: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., local: _Optional[_Union[Record.Local, _Mapping]] = ..., ledger: _Optional[_Union[Record.Ledger, _Mapping]] = ..., multi: _Optional[_Union[Record.Multi, _Mapping]] = ..., offline: _Optional[_Union[Record.Offline, _Mapping]] = ...) -> None: ...
