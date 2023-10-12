import bech32

from eth_utils import to_checksum_address, is_hex_address, to_canonical_address

DEFAULT_BECH32_PREFIX = "fx"


class Address:
    def __init__(self, addr: bytes, prefix: str):
        if prefix is None or prefix == "":
            raise Exception("invalid prefix")
        if len(addr) != 20:
            raise Exception("invalid address")
        self._data = addr
        self._prefix = prefix

    @classmethod
    def from_str(cls, addr: str):
        if is_hex_address(addr):
            data = bytes(to_canonical_address(addr))
            return cls(addr=data, prefix="0x")
        else:
            prefix, data = bech32.bech32_decode(addr)
            data = bytes(bech32.convertbits(data, 5, 8, False))
            return cls(addr=data, prefix=prefix)

    def to_string(self, prefix: str = None) -> str:
        prefix = self._prefix if prefix is None else prefix
        if prefix == "0x":
            return self.to_hex()
        data = bech32.convertbits(self._data, 8, 5)
        return bech32.bech32_encode(prefix, data)

    def to_hex(self) -> str:
        return to_checksum_address(self._data)

    def to_bytes(self) -> bytes:
        return self._data

    def prefix(self) -> str:
        return self._prefix
