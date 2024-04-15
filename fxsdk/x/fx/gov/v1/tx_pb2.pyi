from fxsdk.x.cosmos.msg.v1 import msg_pb2 as _msg_pb2
from fxsdk.x.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from fxsdk.x.fx.gov.v1 import params_pb2 as _params_pb2
from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MsgUpdateParams(_message.Message):
    __slots__ = ["authority", "params"]
    AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    authority: str
    params: _params_pb2.Params
    def __init__(self, authority: _Optional[str] = ..., params: _Optional[_Union[_params_pb2.Params, _Mapping]] = ...) -> None: ...

class MsgUpdateParamsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgUpdateEGFParams(_message.Message):
    __slots__ = ["authority", "params"]
    AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    authority: str
    params: _params_pb2.EGFParams
    def __init__(self, authority: _Optional[str] = ..., params: _Optional[_Union[_params_pb2.EGFParams, _Mapping]] = ...) -> None: ...

class MsgUpdateEGFParamsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
