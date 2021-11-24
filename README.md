## How to use

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

## Compile Proto files as Python files

> If does not have execution permission, run 'chmod +x ./gen-proto.sh`

```shell
# Pull external code
git submodule add -b release/v2.2.x https://github.com/functionx/fx-core.git
git submodule add -b release/v3.1.x https://github.com/cosmos/ibc-go.git
git submodule add -b release/v0.45.x https://github.com/cosmos/cosmos-sdk.git
git submodule update

pip install grpcio
pip install grpcio-tools

./gen-proto.sh
```
