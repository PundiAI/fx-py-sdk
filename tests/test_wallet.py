import unittest

from fxsdk.wallet.address import Address
from fxsdk.wallet.key import PublicKey, PrivateKey, SECP256K1_KEY_TYPE
from fxsdk.wallet.key import mnemonic_to_privkey
from eth_hash.auto import keccak as keccak_256


class TestWallet(unittest.TestCase):
    def test_seed_to_address(self):
        private_key = mnemonic_to_privkey('test test test test test test test test test test test junk')
        self.assertEqual(private_key.to_hex(), 'ac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80')
        self.assertEqual(private_key.to_public_key().to_hex(),
                         '038318535b54105d4a7aae60c08fc45f9687181b4fdfc625bd1a753fa7397fed75')
        self.assertEqual(private_key.to_address(prefix='mx').to_string(),
                         'mx17w0adeg64ky0daxwd2ugyuneellmjgnxqezt98')

    def test_public_key(self):
        pub_key_bytes = bytes.fromhex('038318535b54105d4a7aae60c08fc45f9687181b4fdfc625bd1a753fa7397fed75')
        pub_key = PublicKey(pub_key=pub_key_bytes, key_type=SECP256K1_KEY_TYPE)
        self.assertEqual(pub_key.to_address().to_string(),
                         'fx15428vq2uzwhm3taey9sr9x5vm6tk78ewryy2rg')

    def test_public_key_protobuf_serialization(self):
        pub_key_bytes = bytes.fromhex('02ad0593f884c5784b69d55b8f2ff244443309abd31c90bad2e440b5171d136098')
        pub_key = PublicKey(pub_key=pub_key_bytes, key_type=SECP256K1_KEY_TYPE)
        self.assertEqual(pub_key.to_secp256k1_any().SerializeToString().hex(),
                         '0a1f2f636f736d6f732e63727970746f2e736563703235366b312e5075624b657912230a2102ad0593f884c5784b69d55b8f2ff244443309abd31c90bad2e440b5171d136098')

    def test_private_key_sign(self):
        priv_key_bytes = bytes.fromhex('ac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80')
        priv_key = PrivateKey(priv_key_bytes)
        self.assertEqual(priv_key.to_address('mx').to_string(), 'mx17w0adeg64ky0daxwd2ugyuneellmjgnxqezt98')
        self.assertEqual(priv_key.sign(priv_key_bytes).hex(),
                         '93d0d025c08961da1fc345352a89ecaa60d95715238c1cb699a2cedb3d2db6ed2b8d76d077dc7e1053d7192bf39c2a8ba61bd6e6c6d98d129c2405b21adf2d1800')

    def test_private_key_sign2(self):
        priv_key_bytes = bytes.fromhex('e64e7928d4f6c06f01fefd31f760c51f59a16426e792761cd00529b76501c8a0')
        priv_key = PrivateKey(priv_key_bytes, SECP256K1_KEY_TYPE)
        self.assertEqual(priv_key.to_address('mx').to_string(), 'mx15yk64u7zc9g9k2yr2wmzeva5qgwxps6y9kkkhe')
        self.assertEqual(priv_key.sign(priv_key_bytes).hex(),
                         'ad489e841a6b2806d80c11daa3e1382bbba7e00bf342f88d31df6154c89c3b6b01bdd3055b9e4e94fbe7558b57e6b578eed881f064a47867617307b0bde1ddba')

    def test_keccak256(self):
        data = keccak_256(bytes.fromhex('ac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80'))
        self.assertEqual(data.hex(), '5b2ef0b493f7d7368b311b19a1165c7ad9315c5bec1256fdcf98de11b940aed2')

    def test_address(self):
        address = Address.from_str('mx17w0adeg64ky0daxwd2ugyuneellmjgnxqezt98')
        self.assertEqual(address.to_string(), 'mx17w0adeg64ky0daxwd2ugyuneellmjgnxqezt98')
        self.assertEqual(address.to_hex(),'0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266')


if __name__ == '__main__':
    unittest.main()
