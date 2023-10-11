import unittest

from fxsdk.x.fx.dex.v1.order_pb2 import Direction


class TestProto(unittest.TestCase):
    def test_enum(self):
        buy = Direction.Name(Direction.BUY)
        self.assertEqual(str(buy), 'BUY')


if __name__ == '__main__':
    unittest.main()
