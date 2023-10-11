import unittest

from fxsdk.coin import parse_coins, parse_coin


class TestCoinCase(unittest.TestCase):
    def test_parse_coins(self):
        coins = parse_coins("1000000cusd,2000000FX")
        self.assertEqual(2, len(coins))
        self.assertEqual("1000000", coins[0].amount)
        self.assertEqual("cusd", coins[0].denom)
        self.assertEqual("2000000", coins[1].amount)
        self.assertEqual("FX", coins[1].denom)

    def test_parse_coin(self):
        coin = parse_coin("1000000cusd")
        self.assertEqual("1000000", coin.amount)
        self.assertEqual("cusd", coin.denom)


if __name__ == '__main__':
    unittest.main()
