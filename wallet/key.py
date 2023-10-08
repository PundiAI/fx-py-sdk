import hashlib
import bech32
import ecdsa
import hdwallets
import mnemonic

from google.protobuf.any_pb2 import Any

from x.cosmos.crypto.secp256k1.keys_pb2 import PubKey
from wallet.address import DEFAULT_BECH32_HRP

DEFAULT_DERIVATION_PATH = "m/44'/60'/0'/0/0"


class PublicKey:
    def __init__(self, key: bytes):
        self._pub_key = key

    def to_address(self, *, hrp: str = DEFAULT_BECH32_HRP) -> str:
        s = hashlib.new("sha256", self._pub_key).digest()
        r = hashlib.new("ripemd160", s).digest()
        five_bit_r = bech32.convertbits(r, 8, 5)
        assert five_bit_r is not None, "Unsuccessful bech32.convertbits call"
        return bech32.bech32_encode(hrp, five_bit_r)

    def to_secp256k1_any(self) -> Any:
        key = PubKey(key=self._pub_key).SerializeToString()
        return Any(type_url='/ethermint.crypto.v1.ethsecp256k1.PubKey', value=key)

    def to_hex(self) -> str:
        return bytes.hex(self._pub_key)


class PrivateKey:

    def __init__(self, key: bytes) -> None:
        self._priv_key = key

    def to_public_key(self) -> PublicKey:
        privkey_obj = ecdsa.SigningKey.from_string(
            self._priv_key, curve=ecdsa.SECP256k1)
        pubkey_obj = privkey_obj.get_verifying_key()
        return PublicKey(pubkey_obj.to_string("compressed"))

    def to_address(self, hrp: str = DEFAULT_BECH32_HRP) -> str:
        return self.to_public_key().to_address(hrp=hrp)

    def to_hex(self) -> str:
        return bytes.hex(self._priv_key)

    def sign(self, message_bytes: bytes) -> bytes:
        privkey = ecdsa.SigningKey.from_string(
            self._priv_key, curve=ecdsa.SECP256k1)
        signature_compact = privkey.sign_deterministic(
            message_bytes, hashfunc=hashlib.sha256, sigencode=ecdsa.util.sigencode_string_canonize
        )
        return signature_compact


def generate_mnemonic() -> str:
    return mnemonic.Mnemonic(language="english").generate(strength=256)


def mnemonic_to_privkey(phrase: str, path: str = DEFAULT_DERIVATION_PATH) -> PrivateKey:
    """Get a private key from a mnemonic seed and a derivation path.

    Assumes a BIP39 mnemonic seed with no passphrase. Raises
    `cosmospy.BIP32DerivationError` if the resulting private key is
    invalid.
    """
    seed_bytes = mnemonic.Mnemonic.to_seed(phrase, passphrase="")
    hd_wallet = hdwallets.BIP32.from_seed(seed_bytes)
    # This can raise a `hdwallets.BIP32DerivationError` (which we alias so
    # that the same exception type is also in the `cosmospy` namespace).
    derived_privkey = hd_wallet.get_privkey_from_path(path)

    return PrivateKey(derived_privkey)


def pubkey_to_address(pubkey: bytes, *, hrp: str = DEFAULT_BECH32_HRP) -> str:
    s = hashlib.new("sha256", pubkey).digest()
    r = hashlib.new("ripemd160", s).digest()
    five_bit_r = bech32.convertbits(r, 8, 5)
    assert five_bit_r is not None, "Unsuccessful bech32.convertbits call"
    return bech32.bech32_encode(hrp, five_bit_r)
