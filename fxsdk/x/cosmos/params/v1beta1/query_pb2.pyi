from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.api import annotations_pb2 as _annotations_pb2
from fxpysdk.fxsdk.x.cosmos.params.v1beta1 import params_pb2 as _params_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryParamsRequest(_message.Message):
    __slots__ = ["subspace", "key"]
    SUBSPACE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    subspace: str
    key: str
    def __init__(self, subspace: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...

class QueryParamsResponse(_message.Message):
    __slots__ = ["param"]
    PARAM_FIELD_NUMBER: _ClassVar[int]
    param: _params_pb2.ParamChange
    def __init__(self, param: _Optional[_Union[_params_pb2.ParamChange, _Mapping]] = ...) -> None: ...

class QuerySubspacesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QuerySubspacesResponse(_message.Message):
    __slots__ = ["subspaces"]
    SUBSPACES_FIELD_NUMBER: _ClassVar[int]
    subspaces: _containers.RepeatedCompositeFieldContainer[Subspace]
    def __init__(self, subspaces: _Optional[_Iterable[_Union[Subspace, _Mapping]]] = ...) -> None: ...

class Subspace(_message.Message):
    __slots__ = ["subspace", "keys"]
    SUBSPACE_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    subspace: str
    keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, subspace: _Optional[str] = ..., keys: _Optional[_Iterable[str]] = ...) -> None: ...
