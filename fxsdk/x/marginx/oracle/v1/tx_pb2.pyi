from gogoproto import gogo_pb2 as _gogo_pb2
from marginx.oracle.v1 import types_pb2 as _types_pb2
from cosmos.msg.v1 import msg_pb2 as _msg_pb2
from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MsgBatchSubmitOracleAnswers(_message.Message):
    __slots__ = ["from_address", "answers"]
    FROM_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ANSWERS_FIELD_NUMBER: _ClassVar[int]
    from_address: str
    answers: _containers.RepeatedCompositeFieldContainer[OracleAnswer]
    def __init__(self, from_address: _Optional[str] = ..., answers: _Optional[_Iterable[_Union[OracleAnswer, _Mapping]]] = ...) -> None: ...

class MsgBatchSubmitOracleAnswersResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class OracleAnswer(_message.Message):
    __slots__ = ["symbol", "height", "answer", "signature"]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    height: int
    answer: str
    signature: bytes
    def __init__(self, symbol: _Optional[str] = ..., height: _Optional[int] = ..., answer: _Optional[str] = ..., signature: _Optional[bytes] = ...) -> None: ...

class MsgUpdateAggregator(_message.Message):
    __slots__ = ["authority", "aggregator"]
    AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    AGGREGATOR_FIELD_NUMBER: _ClassVar[int]
    authority: str
    aggregator: _types_pb2.Aggregator
    def __init__(self, authority: _Optional[str] = ..., aggregator: _Optional[_Union[_types_pb2.Aggregator, _Mapping]] = ...) -> None: ...

class MsgUpdateAggregatorResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgPresetOracle(_message.Message):
    __slots__ = ["authority", "markets", "prices", "aggregators"]
    AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    MARKETS_FIELD_NUMBER: _ClassVar[int]
    PRICES_FIELD_NUMBER: _ClassVar[int]
    AGGREGATORS_FIELD_NUMBER: _ClassVar[int]
    authority: str
    markets: _containers.RepeatedCompositeFieldContainer[_types_pb2.Market]
    prices: _containers.RepeatedCompositeFieldContainer[_types_pb2.Price]
    aggregators: _containers.RepeatedCompositeFieldContainer[_types_pb2.Aggregator]
    def __init__(self, authority: _Optional[str] = ..., markets: _Optional[_Iterable[_Union[_types_pb2.Market, _Mapping]]] = ..., prices: _Optional[_Iterable[_Union[_types_pb2.Price, _Mapping]]] = ..., aggregators: _Optional[_Iterable[_Union[_types_pb2.Aggregator, _Mapping]]] = ...) -> None: ...

class MsgPresetOracleResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
