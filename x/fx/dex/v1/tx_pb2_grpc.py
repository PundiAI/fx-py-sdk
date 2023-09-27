# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from x.fx.dex.v1 import tx_pb2 as fx_dot_dex_dot_v1_dot_tx__pb2


class MsgStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateOrder = channel.unary_unary(
                '/fx.dex.v1.Msg/CreateOrder',
                request_serializer=fx_dot_dex_dot_v1_dot_tx__pb2.MsgCreateOrder.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_tx__pb2.MsgCreateOrderResponse.FromString,
                )
        self.CancelOrder = channel.unary_unary(
                '/fx.dex.v1.Msg/CancelOrder',
                request_serializer=fx_dot_dex_dot_v1_dot_tx__pb2.MsgCancelOrder.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_tx__pb2.MsgCancelOrderResponse.FromString,
                )
        self.AddMargin = channel.unary_unary(
                '/fx.dex.v1.Msg/AddMargin',
                request_serializer=fx_dot_dex_dot_v1_dot_tx__pb2.MsgAddMargin.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_tx__pb2.MsgAddMarginResp.FromString,
                )
        self.ClosePosition = channel.unary_unary(
                '/fx.dex.v1.Msg/ClosePosition',
                request_serializer=fx_dot_dex_dot_v1_dot_tx__pb2.MsgClosePosition.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_tx__pb2.MsgClosePositionResp.FromString,
                )
        self.LiquidationPosition = channel.unary_unary(
                '/fx.dex.v1.Msg/LiquidationPosition',
                request_serializer=fx_dot_dex_dot_v1_dot_tx__pb2.MsgLiquidationPosition.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_tx__pb2.MsgLiquidationPositionResp.FromString,
                )
        self.FundDexPool = channel.unary_unary(
                '/fx.dex.v1.Msg/FundDexPool',
                request_serializer=fx_dot_dex_dot_v1_dot_tx__pb2.MsgFundDexPool.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_tx__pb2.MsgFundDexPoolResp.FromString,
                )


class MsgServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddMargin(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClosePosition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LiquidationPosition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FundDexPool(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateOrder,
                    request_deserializer=fx_dot_dex_dot_v1_dot_tx__pb2.MsgCreateOrder.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_tx__pb2.MsgCreateOrderResponse.SerializeToString,
            ),
            'CancelOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelOrder,
                    request_deserializer=fx_dot_dex_dot_v1_dot_tx__pb2.MsgCancelOrder.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_tx__pb2.MsgCancelOrderResponse.SerializeToString,
            ),
            'AddMargin': grpc.unary_unary_rpc_method_handler(
                    servicer.AddMargin,
                    request_deserializer=fx_dot_dex_dot_v1_dot_tx__pb2.MsgAddMargin.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_tx__pb2.MsgAddMarginResp.SerializeToString,
            ),
            'ClosePosition': grpc.unary_unary_rpc_method_handler(
                    servicer.ClosePosition,
                    request_deserializer=fx_dot_dex_dot_v1_dot_tx__pb2.MsgClosePosition.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_tx__pb2.MsgClosePositionResp.SerializeToString,
            ),
            'LiquidationPosition': grpc.unary_unary_rpc_method_handler(
                    servicer.LiquidationPosition,
                    request_deserializer=fx_dot_dex_dot_v1_dot_tx__pb2.MsgLiquidationPosition.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_tx__pb2.MsgLiquidationPositionResp.SerializeToString,
            ),
            'FundDexPool': grpc.unary_unary_rpc_method_handler(
                    servicer.FundDexPool,
                    request_deserializer=fx_dot_dex_dot_v1_dot_tx__pb2.MsgFundDexPool.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_tx__pb2.MsgFundDexPoolResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'fx.dex.v1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Msg/CreateOrder',
            fx_dot_dex_dot_v1_dot_tx__pb2.MsgCreateOrder.SerializeToString,
            fx_dot_dex_dot_v1_dot_tx__pb2.MsgCreateOrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CancelOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Msg/CancelOrder',
            fx_dot_dex_dot_v1_dot_tx__pb2.MsgCancelOrder.SerializeToString,
            fx_dot_dex_dot_v1_dot_tx__pb2.MsgCancelOrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddMargin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Msg/AddMargin',
            fx_dot_dex_dot_v1_dot_tx__pb2.MsgAddMargin.SerializeToString,
            fx_dot_dex_dot_v1_dot_tx__pb2.MsgAddMarginResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClosePosition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Msg/ClosePosition',
            fx_dot_dex_dot_v1_dot_tx__pb2.MsgClosePosition.SerializeToString,
            fx_dot_dex_dot_v1_dot_tx__pb2.MsgClosePositionResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LiquidationPosition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Msg/LiquidationPosition',
            fx_dot_dex_dot_v1_dot_tx__pb2.MsgLiquidationPosition.SerializeToString,
            fx_dot_dex_dot_v1_dot_tx__pb2.MsgLiquidationPositionResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FundDexPool(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Msg/FundDexPool',
            fx_dot_dex_dot_v1_dot_tx__pb2.MsgFundDexPool.SerializeToString,
            fx_dot_dex_dot_v1_dot_tx__pb2.MsgFundDexPoolResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
