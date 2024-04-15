from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import any_pb2 as _any_pb2
from fxsdk.x.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from fxsdk.x.cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BasicAllowance(_message.Message):
    __slots__ = ["spend_limit", "expiration"]
    SPEND_LIMIT_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    spend_limit: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    expiration: _timestamp_pb2.Timestamp
    def __init__(self, spend_limit: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ..., expiration: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PeriodicAllowance(_message.Message):
    __slots__ = ["basic", "period", "period_spend_limit", "period_can_spend", "period_reset"]
    BASIC_FIELD_NUMBER: _ClassVar[int]
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    PERIOD_SPEND_LIMIT_FIELD_NUMBER: _ClassVar[int]
    PERIOD_CAN_SPEND_FIELD_NUMBER: _ClassVar[int]
    PERIOD_RESET_FIELD_NUMBER: _ClassVar[int]
    basic: BasicAllowance
    period: _duration_pb2.Duration
    period_spend_limit: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    period_can_spend: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    period_reset: _timestamp_pb2.Timestamp
    def __init__(self, basic: _Optional[_Union[BasicAllowance, _Mapping]] = ..., period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., period_spend_limit: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ..., period_can_spend: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ..., period_reset: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AllowedMsgAllowance(_message.Message):
    __slots__ = ["allowance", "allowed_messages"]
    ALLOWANCE_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    allowance: _any_pb2.Any
    allowed_messages: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, allowance: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., allowed_messages: _Optional[_Iterable[str]] = ...) -> None: ...

class Grant(_message.Message):
    __slots__ = ["granter", "grantee", "allowance"]
    GRANTER_FIELD_NUMBER: _ClassVar[int]
    GRANTEE_FIELD_NUMBER: _ClassVar[int]
    ALLOWANCE_FIELD_NUMBER: _ClassVar[int]
    granter: str
    grantee: str
    allowance: _any_pb2.Any
    def __init__(self, granter: _Optional[str] = ..., grantee: _Optional[str] = ..., allowance: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
