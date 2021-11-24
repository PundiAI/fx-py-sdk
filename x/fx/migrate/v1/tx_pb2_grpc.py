# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from x.fx.migrate.v1 import tx_pb2 as fx_dot_migrate_dot_v1_dot_tx__pb2


class MsgStub(object):
    """Msg defines the state transitions possible within gravity
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MigrateAccount = channel.unary_unary(
                '/fx.migrate.v1.Msg/MigrateAccount',
                request_serializer=fx_dot_migrate_dot_v1_dot_tx__pb2.MsgMigrateAccount.SerializeToString,
                response_deserializer=fx_dot_migrate_dot_v1_dot_tx__pb2.MsgMigrateAccountResponse.FromString,
                )


class MsgServicer(object):
    """Msg defines the state transitions possible within gravity
    """

    def MigrateAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MigrateAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.MigrateAccount,
                    request_deserializer=fx_dot_migrate_dot_v1_dot_tx__pb2.MsgMigrateAccount.FromString,
                    response_serializer=fx_dot_migrate_dot_v1_dot_tx__pb2.MsgMigrateAccountResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'fx.migrate.v1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the state transitions possible within gravity
    """

    @staticmethod
    def MigrateAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.migrate.v1.Msg/MigrateAccount',
            fx_dot_migrate_dot_v1_dot_tx__pb2.MsgMigrateAccount.SerializeToString,
            fx_dot_migrate_dot_v1_dot_tx__pb2.MsgMigrateAccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
