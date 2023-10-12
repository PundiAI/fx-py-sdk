import unittest

from fxsdk.client.crosschain import CrossChainClient

grpc_cli = CrossChainClient('https://fx-grpc.functionx.io')


class TestCrossChainClientQuery(unittest.TestCase):

    def test_query_channel(self):
        channel = grpc_cli.query_channel('channel-0')
        print(channel)

    def test_query_channels(self):
        channels = grpc_cli.query_channels()
        print(channels)

    def test_get_fee(self):
        fast_fee = grpc_cli.get_fast('ethereum', 'FX')
        print(fast_fee)


if __name__ == '__main__':
    unittest.main()
