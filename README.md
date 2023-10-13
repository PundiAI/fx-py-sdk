# FunctionX Python SDK

[![PyPI version](https://badge.fury.io/py/fx-py-sdk.svg)](https://badge.fury.io/py/fx-py-sdk)

## Install

```shell
pip install fx-py-sdk
```

## Use

```python
from fxsdk.client.grpc import Client
from fxsdk.wallet.builder import TxBuilder
from fxsdk.x.cosmos.base.v1beta1.coin_pb2 import Coin

if __name__ == '__main__':
    grpc_cli = Client(url='127.0.0.1:9090')
    mnemonic = 'test test test test test test test test test test test junk'
    prefix = 'fx'
    
    tx_builder = TxBuilder.from_mnemonic(mnemonic=mnemonic, prefix=prefix)
    to = tx_builder.from_address().to_string()
    amount = [Coin(amount='100', denom='FX')]
    tx_response = grpc_cli.bank_send(tx_builder, to, amount)
    print(tx_response)
```

## Development

### 1. Clone the code to local

```shell
git clone https://github.com/functionx/fx-py-sdk.git

cd fx-py-sdk
```

### 2. Build the Python virtual environment for the current project

* Create the virtual directory venv

```
python -m venv venv
```

* Activating the Virtual Environment

```
source ./venv/bin/activate
```
> Windows: venv\Scripts\activate

### 3. Installation Project Dependence

```
pip install -r requirements.txt
```

### 4. Compile Proto files as Python files

> If does not have execution permission, run 'chmod +x ./gen-proto.sh`

```shell
# Pull external code
git submodule update --init --recursive --remote

./gen-proto.sh
```

### 5. Build Project

```shell
python -m build
```

## License

[Apache License 2.0](LICENSE)
