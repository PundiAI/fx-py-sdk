from cosmos.app.v1alpha1 import config_pb2 as _config_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryConfigRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryConfigResponse(_message.Message):
    __slots__ = ["config"]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: _config_pb2.Config
    def __init__(self, config: _Optional[_Union[_config_pb2.Config, _Mapping]] = ...) -> None: ...
