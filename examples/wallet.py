from fxsdk.wallet.builder import TxBuilder
from fxsdk.wallet.key import PrivateKey

if __name__ == '__main__':
    mnemonic = 'test test test test test test test test test test test junk'
    prefix = 'mx'

    tx_builder1 = TxBuilder.from_mnemonic(mnemonic=mnemonic, path="m/44'/60'/0'/0/1", prefix=prefix)

    tx_builder2 = TxBuilder.from_mnemonic_with_index(mnemonic=mnemonic, index=1, prefix=prefix)

    private_key = PrivateKey.from_hex('59c6995e998f97a5a0044966f0945389dc9e86dae88c7a8412f4603b6b78690d')
    tx_builder3 = TxBuilder(private_key=private_key, prefix=prefix)

    assert tx_builder1.from_address().to_string() == tx_builder2.from_address().to_string()
    assert tx_builder1.from_address().to_string() == tx_builder3.from_address().to_string()
