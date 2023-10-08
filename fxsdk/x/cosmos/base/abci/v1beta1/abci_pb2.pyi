from gogoproto import gogo_pb2 as _gogo_pb2
from tendermint.abci import types_pb2 as _types_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TxResponse(_message.Message):
    __slots__ = ["height", "txhash", "codespace", "code", "data", "raw_log", "logs", "info", "gas_wanted", "gas_used", "tx", "timestamp", "events"]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    TXHASH_FIELD_NUMBER: _ClassVar[int]
    CODESPACE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    RAW_LOG_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    GAS_WANTED_FIELD_NUMBER: _ClassVar[int]
    GAS_USED_FIELD_NUMBER: _ClassVar[int]
    TX_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    height: int
    txhash: str
    codespace: str
    code: int
    data: str
    raw_log: str
    logs: _containers.RepeatedCompositeFieldContainer[ABCIMessageLog]
    info: str
    gas_wanted: int
    gas_used: int
    tx: _any_pb2.Any
    timestamp: str
    events: _containers.RepeatedCompositeFieldContainer[_types_pb2.Event]
    def __init__(self, height: _Optional[int] = ..., txhash: _Optional[str] = ..., codespace: _Optional[str] = ..., code: _Optional[int] = ..., data: _Optional[str] = ..., raw_log: _Optional[str] = ..., logs: _Optional[_Iterable[_Union[ABCIMessageLog, _Mapping]]] = ..., info: _Optional[str] = ..., gas_wanted: _Optional[int] = ..., gas_used: _Optional[int] = ..., tx: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., timestamp: _Optional[str] = ..., events: _Optional[_Iterable[_Union[_types_pb2.Event, _Mapping]]] = ...) -> None: ...

class ABCIMessageLog(_message.Message):
    __slots__ = ["msg_index", "log", "events"]
    MSG_INDEX_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    msg_index: int
    log: str
    events: _containers.RepeatedCompositeFieldContainer[StringEvent]
    def __init__(self, msg_index: _Optional[int] = ..., log: _Optional[str] = ..., events: _Optional[_Iterable[_Union[StringEvent, _Mapping]]] = ...) -> None: ...

class StringEvent(_message.Message):
    __slots__ = ["type", "attributes"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    type: str
    attributes: _containers.RepeatedCompositeFieldContainer[Attribute]
    def __init__(self, type: _Optional[str] = ..., attributes: _Optional[_Iterable[_Union[Attribute, _Mapping]]] = ...) -> None: ...

class Attribute(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class GasInfo(_message.Message):
    __slots__ = ["gas_wanted", "gas_used"]
    GAS_WANTED_FIELD_NUMBER: _ClassVar[int]
    GAS_USED_FIELD_NUMBER: _ClassVar[int]
    gas_wanted: int
    gas_used: int
    def __init__(self, gas_wanted: _Optional[int] = ..., gas_used: _Optional[int] = ...) -> None: ...

class Result(_message.Message):
    __slots__ = ["data", "log", "events", "msg_responses"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    MSG_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    log: str
    events: _containers.RepeatedCompositeFieldContainer[_types_pb2.Event]
    msg_responses: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, data: _Optional[bytes] = ..., log: _Optional[str] = ..., events: _Optional[_Iterable[_Union[_types_pb2.Event, _Mapping]]] = ..., msg_responses: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class SimulationResponse(_message.Message):
    __slots__ = ["gas_info", "result"]
    GAS_INFO_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    gas_info: GasInfo
    result: Result
    def __init__(self, gas_info: _Optional[_Union[GasInfo, _Mapping]] = ..., result: _Optional[_Union[Result, _Mapping]] = ...) -> None: ...

class MsgData(_message.Message):
    __slots__ = ["msg_type", "data"]
    MSG_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    msg_type: str
    data: bytes
    def __init__(self, msg_type: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class TxMsgData(_message.Message):
    __slots__ = ["data", "msg_responses"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MSG_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[MsgData]
    msg_responses: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, data: _Optional[_Iterable[_Union[MsgData, _Mapping]]] = ..., msg_responses: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class SearchTxsResult(_message.Message):
    __slots__ = ["total_count", "count", "page_number", "page_total", "limit", "txs"]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PAGE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOTAL_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    TXS_FIELD_NUMBER: _ClassVar[int]
    total_count: int
    count: int
    page_number: int
    page_total: int
    limit: int
    txs: _containers.RepeatedCompositeFieldContainer[TxResponse]
    def __init__(self, total_count: _Optional[int] = ..., count: _Optional[int] = ..., page_number: _Optional[int] = ..., page_total: _Optional[int] = ..., limit: _Optional[int] = ..., txs: _Optional[_Iterable[_Union[TxResponse, _Mapping]]] = ...) -> None: ...
