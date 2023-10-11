import unittest
from decimal import Decimal

from fxsdk.dec import dec_to_str, dec_from_str


class TestDecCase(unittest.TestCase):
    def test_dec_to_str(self):
        res = dec_to_str(Decimal('1.000000000000000000'))
        self.assertEqual(res, '1000000')

    def test_dec_from_str(self):
        res = dec_from_str('1.000000000000000000')
        self.assertEqual(res, Decimal('0.000001000000000000'))


if __name__ == '__main__':
    unittest.main()
