from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SendAuthorization(_message.Message):
    __slots__ = ["spend_limit"]
    SPEND_LIMIT_FIELD_NUMBER: _ClassVar[int]
    spend_limit: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    def __init__(self, spend_limit: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ...) -> None: ...
