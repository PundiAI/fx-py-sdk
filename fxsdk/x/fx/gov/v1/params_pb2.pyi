from fxsdk.x.cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from fxsdk.x.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Params(_message.Message):
    __slots__ = ["msg_type", "min_deposit", "min_initial_deposit", "voting_period", "quorum", "max_deposit_period", "threshold", "veto_threshold"]
    MSG_TYPE_FIELD_NUMBER: _ClassVar[int]
    MIN_DEPOSIT_FIELD_NUMBER: _ClassVar[int]
    MIN_INITIAL_DEPOSIT_FIELD_NUMBER: _ClassVar[int]
    VOTING_PERIOD_FIELD_NUMBER: _ClassVar[int]
    QUORUM_FIELD_NUMBER: _ClassVar[int]
    MAX_DEPOSIT_PERIOD_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    VETO_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    msg_type: str
    min_deposit: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    min_initial_deposit: _coin_pb2.Coin
    voting_period: _duration_pb2.Duration
    quorum: str
    max_deposit_period: _duration_pb2.Duration
    threshold: str
    veto_threshold: str
    def __init__(self, msg_type: _Optional[str] = ..., min_deposit: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ..., min_initial_deposit: _Optional[_Union[_coin_pb2.Coin, _Mapping]] = ..., voting_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., quorum: _Optional[str] = ..., max_deposit_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., threshold: _Optional[str] = ..., veto_threshold: _Optional[str] = ...) -> None: ...

class EGFParams(_message.Message):
    __slots__ = ["egf_deposit_threshold", "claim_ratio"]
    EGF_DEPOSIT_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    CLAIM_RATIO_FIELD_NUMBER: _ClassVar[int]
    egf_deposit_threshold: _coin_pb2.Coin
    claim_ratio: str
    def __init__(self, egf_deposit_threshold: _Optional[_Union[_coin_pb2.Coin, _Mapping]] = ..., claim_ratio: _Optional[str] = ...) -> None: ...
