from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos.authz.v1beta1 import authz_pb2 as _authz_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ["authorization"]
    AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    authorization: _containers.RepeatedCompositeFieldContainer[_authz_pb2.GrantAuthorization]
    def __init__(self, authorization: _Optional[_Iterable[_Union[_authz_pb2.GrantAuthorization, _Mapping]]] = ...) -> None: ...
