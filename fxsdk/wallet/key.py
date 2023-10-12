import hashlib
import ecdsa
import hdwallets
import coincurve

from mnemonic import Mnemonic
from eth_hash.auto import keccak as keccak_256
from google.protobuf.any_pb2 import Any

from fxsdk.x.cosmos.crypto.secp256k1.keys_pb2 import PubKey as secp256k1PubKey
from fxsdk.x.ethermint.crypto.v1.ethsecp256k1.keys_pb2 import PubKey as ethsecp256k1PubKey
from fxsdk.wallet.address import DEFAULT_BECH32_PREFIX, Address

ETH_DERIVATION_PATH = "m/44'/60'/0'/0/0"
ETHSECP256K1_KEY_TYPE = 'eth_secp256k1'
ETHSECP256K1_PUBLICK_TYPE_URL = '/ethermint.crypto.v1.ethsecp256k1.PubKey'

COSMOS_DERIVATION_PATH = "m/44'/118'/0'/0/0"
SECP256K1_KEY_TYPE = 'secp256k1'
SECP256K1_PUBLICK_TYPE_URL = '/cosmos.crypto.secp256k1.PubKey'


class PublicKey:
    def __init__(self, pub_key: bytes, key_type: str = ETHSECP256K1_KEY_TYPE):
        self._pub_key = pub_key
        self._key_type = key_type

    def to_address(self, prefix: str = DEFAULT_BECH32_PREFIX) -> Address:
        if self._key_type == SECP256K1_KEY_TYPE:
            h = hashlib.new("sha256", self._pub_key).digest()
            data = hashlib.new("ripemd160", h).digest()
            if prefix == "0x":
                raise Exception("secp256k1 not support 0x prefix address")
        else:
            pubkey_obj = ecdsa.keys.VerifyingKey.from_string(self._pub_key, curve=ecdsa.SECP256k1)
            data = keccak_256(pubkey_obj.to_string("raw"))[-20:]

        return Address(addr=data, prefix=prefix)

    def to_secp256k1_any(self) -> Any:
        if self._key_type == SECP256K1_KEY_TYPE:
            key = secp256k1PubKey(key=self._pub_key).SerializeToString()
            public_type_url = SECP256K1_PUBLICK_TYPE_URL
            return Any(type_url=public_type_url, value=key)
        else:
            key = ethsecp256k1PubKey(key=self._pub_key).SerializeToString()
            public_type_url = ETHSECP256K1_PUBLICK_TYPE_URL
            return Any(type_url=public_type_url, value=key)

    def to_hex(self) -> str:
        return bytes.hex(self._pub_key)


class PrivateKey:

    def __init__(self, priv_key: bytes, key_type: str = ETHSECP256K1_KEY_TYPE) -> None:
        self._priv_key = priv_key
        self._key_type = key_type

    def with_key_type(self, key_type):
        self._key_type = key_type

    def to_public_key(self) -> PublicKey:
        privkey_obj = ecdsa.SigningKey.from_string(self._priv_key, curve=ecdsa.SECP256k1)
        pubkey_obj = privkey_obj.get_verifying_key()
        return PublicKey(pub_key=pubkey_obj.to_string("compressed"), key_type=self._key_type)

    def to_address(self, prefix: str = DEFAULT_BECH32_PREFIX) -> Address:
        return self.to_public_key().to_address(prefix=prefix)

    def to_hex(self) -> str:
        return bytes.hex(self._priv_key)

    def sign(self, message_bytes: bytes) -> bytes:
        if self._key_type == SECP256K1_KEY_TYPE:
            privkey = ecdsa.SigningKey.from_string(self._priv_key, curve=ecdsa.SECP256k1)
            signature_compact = privkey.sign_deterministic(
                data=message_bytes, hashfunc=hashlib.sha256, sigencode=ecdsa.util.sigencode_string_canonize
            )
        else:
            if len(message_bytes) != 32:
                message_bytes = keccak_256(message_bytes)
            signature_compact = coincurve.keys.PrivateKey(self._priv_key).sign_recoverable(
                message=message_bytes, hasher=None,
            )

        return signature_compact


def generate_mnemonic() -> str:
    return Mnemonic(language="english").generate(strength=256)


def mnemonic_to_privkey(mnemonic: str, passphrase: str = '', path: str = ETH_DERIVATION_PATH,
                        key_type: str = ETHSECP256K1_KEY_TYPE) -> PrivateKey:
    """Get a private key from a mnemonic seed and a derivation path.
    """
    seed_bytes = Mnemonic.to_seed(mnemonic=mnemonic, passphrase=passphrase)
    hd_wallet = hdwallets.BIP32.from_seed(seed_bytes)
    derived_privkey = hd_wallet.get_privkey_from_path(path)
    return PrivateKey(priv_key=derived_privkey, key_type=key_type)


def pubkey_to_address(pubkey: bytes, prefix: str = DEFAULT_BECH32_PREFIX,
                      key_type: str = ETHSECP256K1_KEY_TYPE, ) -> str:
    return PublicKey(pub_key=pubkey, key_type=key_type).to_address(prefix).to_string()
