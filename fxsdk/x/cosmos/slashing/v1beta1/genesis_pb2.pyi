from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from fxpysdk.fxsdk.x.cosmos.slashing.v1beta1 import slashing_pb2 as _slashing_pb2
from fxpysdk.fxsdk.x.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ["params", "signing_infos", "missed_blocks"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    SIGNING_INFOS_FIELD_NUMBER: _ClassVar[int]
    MISSED_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    params: _slashing_pb2.Params
    signing_infos: _containers.RepeatedCompositeFieldContainer[SigningInfo]
    missed_blocks: _containers.RepeatedCompositeFieldContainer[ValidatorMissedBlocks]
    def __init__(self, params: _Optional[_Union[_slashing_pb2.Params, _Mapping]] = ..., signing_infos: _Optional[_Iterable[_Union[SigningInfo, _Mapping]]] = ..., missed_blocks: _Optional[_Iterable[_Union[ValidatorMissedBlocks, _Mapping]]] = ...) -> None: ...

class SigningInfo(_message.Message):
    __slots__ = ["address", "validator_signing_info"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_SIGNING_INFO_FIELD_NUMBER: _ClassVar[int]
    address: str
    validator_signing_info: _slashing_pb2.ValidatorSigningInfo
    def __init__(self, address: _Optional[str] = ..., validator_signing_info: _Optional[_Union[_slashing_pb2.ValidatorSigningInfo, _Mapping]] = ...) -> None: ...

class ValidatorMissedBlocks(_message.Message):
    __slots__ = ["address", "missed_blocks"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MISSED_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    address: str
    missed_blocks: _containers.RepeatedCompositeFieldContainer[MissedBlock]
    def __init__(self, address: _Optional[str] = ..., missed_blocks: _Optional[_Iterable[_Union[MissedBlock, _Mapping]]] = ...) -> None: ...

class MissedBlock(_message.Message):
    __slots__ = ["index", "missed"]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    MISSED_FIELD_NUMBER: _ClassVar[int]
    index: int
    missed: bool
    def __init__(self, index: _Optional[int] = ..., missed: bool = ...) -> None: ...
