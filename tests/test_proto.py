import unittest

from fxsdk.msg import new_tx_from_base64
from fxsdk.x.cosmos.bank.v1beta1.tx_pb2 import MsgSend
from fxsdk.x.fx.dex.v1.order_pb2 import Direction


class TestProto(unittest.TestCase):
    def test_enum(self):
        buy = Direction.Name(Direction.BUY)
        self.assertEqual(str(buy), 'BUY')

    def test_parse_tx(self):
        raw_tx = 'CoYBCoMBChwvY29zbW9zLmJhbmsudjFiZXRhMS5Nc2dTZW5kEmMKKW14MTd3MGFkZWc2NGt5MGRheHdkMnVneXVuZWVsbG1qZ254cWV6dDk4EilteDE3dzBhZGVnNjRreTBkYXh3ZDJ1Z3l1bmVlbGxtamdueHFlenQ5OBoLCgRjdXNkEgMxMDASbwpZCk8KKC9ldGhlcm1pbnQuY3J5cHRvLnYxLmV0aHNlY3AyNTZrMS5QdWJLZXkSIwohA4MYU1tUEF1Keq5gwI/EX5aHGBtP38YlvRp1P6c5f+11EgQKAggBGAISEgoMCgRjdXNkEgQ0NTAwEKD3NhpBlC4qy88pAlxHfRoli+tOr4sgvKuWKOvp/OlD2iK38pgYKEVR0kF3ERbe1cDTnpEvb5Tfa/J3zGcyXYGm/OqRqQA='
        tx = new_tx_from_base64(raw_tx)
        self.assertEqual(len(tx.body.messages), 1)
        self.assertEqual(tx.body.messages[0].type_url, '/cosmos.bank.v1beta1.MsgSend')
        msg_send = MsgSend()
        msg_send.ParseFromString(tx.body.messages[0].value)
        self.assertEqual(msg_send.from_address, 'mx17w0adeg64ky0daxwd2ugyuneellmjgnxqezt98')
        self.assertEqual(msg_send.to_address, 'mx17w0adeg64ky0daxwd2ugyuneellmjgnxqezt98')
        self.assertEqual(len(msg_send.amount), 1)
        self.assertEqual(msg_send.amount[0].denom, 'cusd')
        self.assertEqual(msg_send.amount[0].amount, '100')
        print(tx)


if __name__ == '__main__':
    unittest.main()
