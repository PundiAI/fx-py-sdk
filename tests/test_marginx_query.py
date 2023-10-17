import unittest

from fxsdk.client.marginx import MarginXClient

grpc_cli = MarginXClient('localhost:9090')

pair_id = 'btc:cusd'
owner = 'mx17w0adeg64ky0daxwd2ugyuneellmjgnxqezt98'


class TestMxClientQuery(unittest.TestCase):

    def test_query_oracle_price(self):
        price = grpc_cli.query_oracle_price(pair_id)
        print(price)

    def test_query_oracle_prices(self):
        prices = grpc_cli.query_oracle_prices()
        print(prices)

    def test_query_oracle_market(self):
        market = grpc_cli.query_oracle_market(pair_id)
        print(market)

    def test_query_oracle_markets(self):
        markets = grpc_cli.query_oracle_markets()
        print(markets)

    def test_query_values(self):
        asset_value = grpc_cli.query_values(owner, pair_id)
        print(asset_value)


if __name__ == '__main__':
    unittest.main()
