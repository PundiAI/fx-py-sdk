# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fx/gravity/v1/attestation.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x66x/gravity/v1/attestation.proto\x12\rfx.gravity.v1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\"c\n\x0b\x41ttestation\x12\x10\n\x08observed\x18\x01 \x01(\x08\x12\r\n\x05votes\x18\x02 \x03(\t\x12\x0e\n\x06height\x18\x03 \x01(\x04\x12#\n\x05\x63laim\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Any\"^\n\nERC20Token\x12\x10\n\x08\x63ontract\x18\x01 \x01(\t\x12>\n\x06\x61mount\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00*\x9e\x01\n\tClaimType\x12\x1a\n\x16\x43LAIM_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12\x43LAIM_TYPE_DEPOSIT\x10\x01\x12\x17\n\x13\x43LAIM_TYPE_WITHDRAW\x10\x02\x12\x1f\n\x1b\x43LAIM_TYPE_ORIGINATED_TOKEN\x10\x03\x12\x1d\n\x19\x43LAIM_TYPE_VALSET_UPDATED\x10\x04\x1a\x04\x88\xa3\x1e\x00\x42.Z,github.com/functionx/fx-core/x/gravity/typesb\x06proto3')

_CLAIMTYPE = DESCRIPTOR.enum_types_by_name['ClaimType']
ClaimType = enum_type_wrapper.EnumTypeWrapper(_CLAIMTYPE)
CLAIM_TYPE_UNSPECIFIED = 0
CLAIM_TYPE_DEPOSIT = 1
CLAIM_TYPE_WITHDRAW = 2
CLAIM_TYPE_ORIGINATED_TOKEN = 3
CLAIM_TYPE_VALSET_UPDATED = 4


_ATTESTATION = DESCRIPTOR.message_types_by_name['Attestation']
_ERC20TOKEN = DESCRIPTOR.message_types_by_name['ERC20Token']
Attestation = _reflection.GeneratedProtocolMessageType('Attestation', (_message.Message,), {
  'DESCRIPTOR' : _ATTESTATION,
  '__module__' : 'fx.gravity.v1.attestation_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.v1.Attestation)
  })
_sym_db.RegisterMessage(Attestation)

ERC20Token = _reflection.GeneratedProtocolMessageType('ERC20Token', (_message.Message,), {
  'DESCRIPTOR' : _ERC20TOKEN,
  '__module__' : 'fx.gravity.v1.attestation_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.v1.ERC20Token)
  })
_sym_db.RegisterMessage(ERC20Token)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/functionx/fx-core/x/gravity/types'
  _CLAIMTYPE._options = None
  _CLAIMTYPE._serialized_options = b'\210\243\036\000'
  _ERC20TOKEN.fields_by_name['amount']._options = None
  _ERC20TOKEN.fields_by_name['amount']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _CLAIMTYPE._serialized_start=297
  _CLAIMTYPE._serialized_end=455
  _ATTESTATION._serialized_start=99
  _ATTESTATION._serialized_end=198
  _ERC20TOKEN._serialized_start=200
  _ERC20TOKEN._serialized_end=294
# @@protoc_insertion_point(module_scope)
