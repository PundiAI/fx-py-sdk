import unittest

from fxsdk.wallet.key import PublicKey, PrivateKey
from fxsdk.wallet.key import mnemonic_to_privkey


class TestWallet(unittest.TestCase):
    def test_seed_to_address(self):
        private_key = mnemonic_to_privkey(
            'test test test test test test test test test test test junk')
        self.assertEqual(private_key.to_hex(), 'ac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80')
        self.assertEqual(private_key.to_public_key().to_hex(),
                         '038318535b54105d4a7aae60c08fc45f9687181b4fdfc625bd1a753fa7397fed75')
        self.assertEqual(private_key.to_address(),
                         'fx15428vq2uzwhm3taey9sr9x5vm6tk78ewryy2rg')

    def test_public_key(self):
        pub_key_bytes = bytes.fromhex(
            '038318535b54105d4a7aae60c08fc45f9687181b4fdfc625bd1a753fa7397fed75')
        pub_key = PublicKey(pub_key_bytes)
        self.assertEqual(pub_key.to_address(),
                         'fx15428vq2uzwhm3taey9sr9x5vm6tk78ewryy2rg')

    def test_public_key_protobuf_serialization(self):
        pub_key_bytes = bytes.fromhex(
            '02ad0593f884c5784b69d55b8f2ff244443309abd31c90bad2e440b5171d136098')
        pub_key = PublicKey(pub_key_bytes)
        self.assertEqual(pub_key.to_secp256k1_any().SerializeToString().hex(),
                         '0a282f65746865726d696e742e63727970746f2e76312e657468736563703235366b312e5075624b657912230a2102ad0593f884c5784b69d55b8f2ff244443309abd31c90bad2e440b5171d136098')

    def test_private_key_sign(self):
        priv_key_bytes = bytes.fromhex(
            '47788d676b3d841f4d608e552a9ed5756e8e54f3cb054aade5c454f6fb3be6ef')
        priv_key = PrivateKey(priv_key_bytes)
        self.assertEqual(priv_key.to_address(),
                         'fx12fv300avzf266qp930ur4g50agajuz6jcsj5tz')
        self.assertEqual(priv_key.sign(priv_key_bytes).hex(),
                         '593fe3673c93ab1e04aa67dacf11040e1711247f33ae6002678abef35829678d44f29dea30dacda2e14dd02261a3433810fb3a981196aff55a548fdba275c404')


if __name__ == '__main__':
    unittest.main()
