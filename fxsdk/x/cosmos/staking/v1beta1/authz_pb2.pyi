from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from fxpysdk.fxsdk.x.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from fxpysdk.fxsdk.x.cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthorizationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    AUTHORIZATION_TYPE_UNSPECIFIED: _ClassVar[AuthorizationType]
    AUTHORIZATION_TYPE_DELEGATE: _ClassVar[AuthorizationType]
    AUTHORIZATION_TYPE_UNDELEGATE: _ClassVar[AuthorizationType]
    AUTHORIZATION_TYPE_REDELEGATE: _ClassVar[AuthorizationType]
AUTHORIZATION_TYPE_UNSPECIFIED: AuthorizationType
AUTHORIZATION_TYPE_DELEGATE: AuthorizationType
AUTHORIZATION_TYPE_UNDELEGATE: AuthorizationType
AUTHORIZATION_TYPE_REDELEGATE: AuthorizationType

class StakeAuthorization(_message.Message):
    __slots__ = ["max_tokens", "allow_list", "deny_list", "authorization_type"]
    class Validators(_message.Message):
        __slots__ = ["address"]
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        address: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, address: _Optional[_Iterable[str]] = ...) -> None: ...
    MAX_TOKENS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_LIST_FIELD_NUMBER: _ClassVar[int]
    DENY_LIST_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    max_tokens: _coin_pb2.Coin
    allow_list: StakeAuthorization.Validators
    deny_list: StakeAuthorization.Validators
    authorization_type: AuthorizationType
    def __init__(self, max_tokens: _Optional[_Union[_coin_pb2.Coin, _Mapping]] = ..., allow_list: _Optional[_Union[StakeAuthorization.Validators, _Mapping]] = ..., deny_list: _Optional[_Union[StakeAuthorization.Validators, _Mapping]] = ..., authorization_type: _Optional[_Union[AuthorizationType, str]] = ...) -> None: ...
