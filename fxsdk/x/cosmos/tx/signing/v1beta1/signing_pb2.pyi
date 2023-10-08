from cosmos.crypto.multisig.v1beta1 import multisig_pb2 as _multisig_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SignMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SIGN_MODE_UNSPECIFIED: _ClassVar[SignMode]
    SIGN_MODE_DIRECT: _ClassVar[SignMode]
    SIGN_MODE_TEXTUAL: _ClassVar[SignMode]
    SIGN_MODE_DIRECT_AUX: _ClassVar[SignMode]
    SIGN_MODE_LEGACY_AMINO_JSON: _ClassVar[SignMode]
    SIGN_MODE_EIP_191: _ClassVar[SignMode]
SIGN_MODE_UNSPECIFIED: SignMode
SIGN_MODE_DIRECT: SignMode
SIGN_MODE_TEXTUAL: SignMode
SIGN_MODE_DIRECT_AUX: SignMode
SIGN_MODE_LEGACY_AMINO_JSON: SignMode
SIGN_MODE_EIP_191: SignMode

class SignatureDescriptors(_message.Message):
    __slots__ = ["signatures"]
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    signatures: _containers.RepeatedCompositeFieldContainer[SignatureDescriptor]
    def __init__(self, signatures: _Optional[_Iterable[_Union[SignatureDescriptor, _Mapping]]] = ...) -> None: ...

class SignatureDescriptor(_message.Message):
    __slots__ = ["public_key", "data", "sequence"]
    class Data(_message.Message):
        __slots__ = ["single", "multi"]
        class Single(_message.Message):
            __slots__ = ["mode", "signature"]
            MODE_FIELD_NUMBER: _ClassVar[int]
            SIGNATURE_FIELD_NUMBER: _ClassVar[int]
            mode: SignMode
            signature: bytes
            def __init__(self, mode: _Optional[_Union[SignMode, str]] = ..., signature: _Optional[bytes] = ...) -> None: ...
        class Multi(_message.Message):
            __slots__ = ["bitarray", "signatures"]
            BITARRAY_FIELD_NUMBER: _ClassVar[int]
            SIGNATURES_FIELD_NUMBER: _ClassVar[int]
            bitarray: _multisig_pb2.CompactBitArray
            signatures: _containers.RepeatedCompositeFieldContainer[SignatureDescriptor.Data]
            def __init__(self, bitarray: _Optional[_Union[_multisig_pb2.CompactBitArray, _Mapping]] = ..., signatures: _Optional[_Iterable[_Union[SignatureDescriptor.Data, _Mapping]]] = ...) -> None: ...
        SINGLE_FIELD_NUMBER: _ClassVar[int]
        MULTI_FIELD_NUMBER: _ClassVar[int]
        single: SignatureDescriptor.Data.Single
        multi: SignatureDescriptor.Data.Multi
        def __init__(self, single: _Optional[_Union[SignatureDescriptor.Data.Single, _Mapping]] = ..., multi: _Optional[_Union[SignatureDescriptor.Data.Multi, _Mapping]] = ...) -> None: ...
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    public_key: _any_pb2.Any
    data: SignatureDescriptor.Data
    sequence: int
    def __init__(self, public_key: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., data: _Optional[_Union[SignatureDescriptor.Data, _Mapping]] = ..., sequence: _Optional[int] = ...) -> None: ...
