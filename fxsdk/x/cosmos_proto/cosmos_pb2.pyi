from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScalarType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SCALAR_TYPE_UNSPECIFIED: _ClassVar[ScalarType]
    SCALAR_TYPE_STRING: _ClassVar[ScalarType]
    SCALAR_TYPE_BYTES: _ClassVar[ScalarType]
SCALAR_TYPE_UNSPECIFIED: ScalarType
SCALAR_TYPE_STRING: ScalarType
SCALAR_TYPE_BYTES: ScalarType
IMPLEMENTS_INTERFACE_FIELD_NUMBER: _ClassVar[int]
implements_interface: _descriptor.FieldDescriptor
ACCEPTS_INTERFACE_FIELD_NUMBER: _ClassVar[int]
accepts_interface: _descriptor.FieldDescriptor
SCALAR_FIELD_NUMBER: _ClassVar[int]
scalar: _descriptor.FieldDescriptor
DECLARE_INTERFACE_FIELD_NUMBER: _ClassVar[int]
declare_interface: _descriptor.FieldDescriptor
DECLARE_SCALAR_FIELD_NUMBER: _ClassVar[int]
declare_scalar: _descriptor.FieldDescriptor

class InterfaceDescriptor(_message.Message):
    __slots__ = ["name", "description"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class ScalarDescriptor(_message.Message):
    __slots__ = ["name", "description", "field_type"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    field_type: _containers.RepeatedScalarFieldContainer[ScalarType]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., field_type: _Optional[_Iterable[_Union[ScalarType, str]]] = ...) -> None: ...
