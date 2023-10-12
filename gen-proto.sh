#!/usr/bin/env bash

set -o errexit -o nounset -o pipefail

OUT_DIR="./fxsdk/x"

[[ -d "$OUT_DIR"  ]] && rm -rf "$OUT_DIR"
[[ ! -d "$OUT_DIR"  ]] && mkdir -p "$OUT_DIR"

proto_dirs=$(find ./proto ./*/proto -path -prune -o -name '*.proto' -print0 | xargs -0 -n1 dirname | sort | uniq)
for dir in $proto_dirs; do
  find "${dir}" -maxdepth 1 -name '*.proto' -print0 | xargs -0 python3 -m grpc_tools.protoc \
    -I="./proto" \
    -I="./fx-core/proto" \
    -I="./cosmos-sdk/proto" \
    -I="./cosmos-sdk/third_party/proto" \
    -I="./ibc-go/proto" \
    -I="./ibc-go/third_party/proto" \
    -I="./ethermint/proto" \
    --python_out="$OUT_DIR" \
    --pyi_out="$OUT_DIR" \
    --grpc_python_out="$OUT_DIR"
done

find "$OUT_DIR" -type d -exec touch {}/__init__.py \;

find "$OUT_DIR" -name '*.py' -print0 | xargs -0 -I{} perl -pi -e 's|from fx.|from fxsdk.x.fx.|g' {}
find "$OUT_DIR" -name '*_pb2.py' -print0 | xargs -0 -I{} perl -pi -e 's|from cosmos.proto import|from fxsdk.x.cosmos_proto import|g' {}
find "$OUT_DIR" -name '*.py' -print0 | xargs -0 -I{} perl -pi -e 's|from cosmos.|from fxsdk.x.cosmos.|g' {}
find "$OUT_DIR" -name '*.py' -print0 | xargs -0 -I{} perl -pi -e 's|from tendermint.|from fxsdk.x.tendermint.|g' {}
find "$OUT_DIR" -name '*_pb2.py' -print0 | xargs -0 -I{} perl -pi -e 's|from gogoproto import|from fxsdk.x.gogoproto import|g' {}
find "$OUT_DIR" -name '*.py' -print0 | xargs -0 -I{} perl -pi -e 's|from ibc.|from fxsdk.x.ibc.|g' {}
find "$OUT_DIR" -name '*.py' -print0 | xargs -0 -I{} perl -pi -e 's|from marginx.|from fxsdk.x.marginx.|g' {}
