import unittest

from fxsdk.client.grpc_client import Client

grpc_cli = Client('localhost:9090')

test_address = "mx17w0adeg64ky0daxwd2ugyuneellmjgnxqezt98"


class TestGrpcClientQuery(unittest.TestCase):

    def test_query_balances(self):
        balances = grpc_cli.query_all_balances(address=test_address)
        print(balances)

    def test_query_balance(self):
        balance = grpc_cli.query_balance(address=test_address, denom="FX")
        print(balance)

        balances = grpc_cli.query_balance(address=test_address, denom="FX")
        print(balances)

    def test_query_account(self):
        account = grpc_cli.query_account_info(address=test_address)
        print(account)

    def test_query_tx(self):
        tx_response = grpc_cli.query_tx("D331D4DAFD2FA19848CA1B97991C0F82BD84F9E4DF18085E27BC2C49B9A9995C")
        print(tx_response)

    def test_query_total_supply(self):
        supply = grpc_cli.query_total_supply()
        print(supply)

    def test_query_validator_list(self):
        validators = grpc_cli.query_validator_list()
        print(validators)

    def test_query_gas_prices(self):
        res = grpc_cli.query_gas_prices()
        print(res)


if __name__ == '__main__':
    unittest.main()
