# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/authz/v1beta1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from x.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from x.cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from x.cosmos.authz.v1beta1 import authz_pb2 as cosmos_dot_authz_dot_v1beta1_dot_authz__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/authz/v1beta1/query.proto\x12\x14\x63osmos.authz.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a cosmos/authz/v1beta1/authz.proto\"\x88\x01\n\x12QueryGrantsRequest\x12\x0f\n\x07granter\x18\x01 \x01(\t\x12\x0f\n\x07grantee\x18\x02 \x01(\t\x12\x14\n\x0cmsg_type_url\x18\x03 \x01(\t\x12:\n\npagination\x18\x04 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x7f\n\x13QueryGrantsResponse\x12+\n\x06grants\x18\x01 \x03(\x0b\x32\x1b.cosmos.authz.v1beta1.Grant\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"h\n\x19QueryGranterGrantsRequest\x12\x0f\n\x07granter\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x93\x01\n\x1aQueryGranterGrantsResponse\x12\x38\n\x06grants\x18\x01 \x03(\x0b\x32(.cosmos.authz.v1beta1.GrantAuthorization\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"h\n\x19QueryGranteeGrantsRequest\x12\x0f\n\x07grantee\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x93\x01\n\x1aQueryGranteeGrantsResponse\x12\x38\n\x06grants\x18\x01 \x03(\x0b\x32(.cosmos.authz.v1beta1.GrantAuthorization\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse2\xe7\x03\n\x05Query\x12\x83\x01\n\x06Grants\x12(.cosmos.authz.v1beta1.QueryGrantsRequest\x1a).cosmos.authz.v1beta1.QueryGrantsResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/cosmos/authz/v1beta1/grants\x12\xaa\x01\n\rGranterGrants\x12/.cosmos.authz.v1beta1.QueryGranterGrantsRequest\x1a\x30.cosmos.authz.v1beta1.QueryGranterGrantsResponse\"6\x82\xd3\xe4\x93\x02\x30\x12./cosmos/authz/v1beta1/grants/granter/{granter}\x12\xaa\x01\n\rGranteeGrants\x12/.cosmos.authz.v1beta1.QueryGranteeGrantsRequest\x1a\x30.cosmos.authz.v1beta1.QueryGranteeGrantsResponse\"6\x82\xd3\xe4\x93\x02\x30\x12./cosmos/authz/v1beta1/grants/grantee/{grantee}B&Z$github.com/cosmos/cosmos-sdk/x/authzb\x06proto3')



_QUERYGRANTSREQUEST = DESCRIPTOR.message_types_by_name['QueryGrantsRequest']
_QUERYGRANTSRESPONSE = DESCRIPTOR.message_types_by_name['QueryGrantsResponse']
_QUERYGRANTERGRANTSREQUEST = DESCRIPTOR.message_types_by_name['QueryGranterGrantsRequest']
_QUERYGRANTERGRANTSRESPONSE = DESCRIPTOR.message_types_by_name['QueryGranterGrantsResponse']
_QUERYGRANTEEGRANTSREQUEST = DESCRIPTOR.message_types_by_name['QueryGranteeGrantsRequest']
_QUERYGRANTEEGRANTSRESPONSE = DESCRIPTOR.message_types_by_name['QueryGranteeGrantsResponse']
QueryGrantsRequest = _reflection.GeneratedProtocolMessageType('QueryGrantsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYGRANTSREQUEST,
  '__module__' : 'cosmos.authz.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.authz.v1beta1.QueryGrantsRequest)
  })
_sym_db.RegisterMessage(QueryGrantsRequest)

QueryGrantsResponse = _reflection.GeneratedProtocolMessageType('QueryGrantsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYGRANTSRESPONSE,
  '__module__' : 'cosmos.authz.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.authz.v1beta1.QueryGrantsResponse)
  })
_sym_db.RegisterMessage(QueryGrantsResponse)

QueryGranterGrantsRequest = _reflection.GeneratedProtocolMessageType('QueryGranterGrantsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYGRANTERGRANTSREQUEST,
  '__module__' : 'cosmos.authz.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.authz.v1beta1.QueryGranterGrantsRequest)
  })
_sym_db.RegisterMessage(QueryGranterGrantsRequest)

QueryGranterGrantsResponse = _reflection.GeneratedProtocolMessageType('QueryGranterGrantsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYGRANTERGRANTSRESPONSE,
  '__module__' : 'cosmos.authz.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.authz.v1beta1.QueryGranterGrantsResponse)
  })
_sym_db.RegisterMessage(QueryGranterGrantsResponse)

QueryGranteeGrantsRequest = _reflection.GeneratedProtocolMessageType('QueryGranteeGrantsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYGRANTEEGRANTSREQUEST,
  '__module__' : 'cosmos.authz.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.authz.v1beta1.QueryGranteeGrantsRequest)
  })
_sym_db.RegisterMessage(QueryGranteeGrantsRequest)

QueryGranteeGrantsResponse = _reflection.GeneratedProtocolMessageType('QueryGranteeGrantsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYGRANTEEGRANTSRESPONSE,
  '__module__' : 'cosmos.authz.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.authz.v1beta1.QueryGranteeGrantsResponse)
  })
_sym_db.RegisterMessage(QueryGranteeGrantsResponse)

_QUERY = DESCRIPTOR.services_by_name['Query']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z$github.com/cosmos/cosmos-sdk/x/authz'
  _QUERY.methods_by_name['Grants']._options = None
  _QUERY.methods_by_name['Grants']._serialized_options = b'\202\323\344\223\002\036\022\034/cosmos/authz/v1beta1/grants'
  _QUERY.methods_by_name['GranterGrants']._options = None
  _QUERY.methods_by_name['GranterGrants']._serialized_options = b'\202\323\344\223\0020\022./cosmos/authz/v1beta1/grants/granter/{granter}'
  _QUERY.methods_by_name['GranteeGrants']._options = None
  _QUERY.methods_by_name['GranteeGrants']._serialized_options = b'\202\323\344\223\0020\022./cosmos/authz/v1beta1/grants/grantee/{grantee}'
  _QUERYGRANTSREQUEST._serialized_start=167
  _QUERYGRANTSREQUEST._serialized_end=303
  _QUERYGRANTSRESPONSE._serialized_start=305
  _QUERYGRANTSRESPONSE._serialized_end=432
  _QUERYGRANTERGRANTSREQUEST._serialized_start=434
  _QUERYGRANTERGRANTSREQUEST._serialized_end=538
  _QUERYGRANTERGRANTSRESPONSE._serialized_start=541
  _QUERYGRANTERGRANTSRESPONSE._serialized_end=688
  _QUERYGRANTEEGRANTSREQUEST._serialized_start=690
  _QUERYGRANTEEGRANTSREQUEST._serialized_end=794
  _QUERYGRANTEEGRANTSRESPONSE._serialized_start=797
  _QUERYGRANTEEGRANTSRESPONSE._serialized_end=944
  _QUERY._serialized_start=947
  _QUERY._serialized_end=1434
# @@protoc_insertion_point(module_scope)
