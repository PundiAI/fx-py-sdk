#!/usr/bin/env bash

set -o errexit -o nounset -o pipefail

command -v shellcheck >/dev/null && shellcheck "$0"

OUT_DIR="./x"

if [ -d "$OUT_DIR"  ]; then
  rm -rf "$OUT_DIR"
fi

if [ ! -d "$OUT_DIR"  ]; then
  mkdir -p "$OUT_DIR"
fi

perl -pi -e 's|ibc.core.client.v1.Height|.ibc.core.client.v1.Height|g' ./fx-core/proto/fx/ibc/applications/transfer/v1/tx.proto

if [ -d "./ibc-go/proto/ibc/applications/transfer"  ]; then
  rm -rf "./ibc-go/proto/ibc/applications/transfer"
fi

proto_dirs=$(find ./*/proto ./cosmos-sdk/third_party/proto -path -prune -o -name '*.proto' -print0 | xargs -0 -n1 dirname | sort | uniq)
for dir in $proto_dirs; do
  python3 -m grpc_tools.protoc \
    -I="./fx-core/proto" \
    -I="./ibc-go/proto" \
    -I="./cosmos-sdk/proto" \
    -I="./cosmos-sdk/third_party/proto" \
    -I="./ibc-go/third_party/proto" \
    --python_out="$OUT_DIR" \
    --grpc_python_out="$OUT_DIR" \
    $(find "${dir}" -maxdepth 1 -name '*.proto')
done

perl -pi -e 's|.ibc.core.client.v1.Height|ibc.core.client.v1.Height|g' ./fx-core/proto/fx/ibc/applications/transfer/v1/tx.proto

find "$OUT_DIR" -type d -exec touch {}/__init__.py \;

find "$OUT_DIR" -name '*_pb2.py' | xargs -I{} perl -pi -e 's|from gogoproto import|from x.gogoproto import|g' {}
find "$OUT_DIR" -name '*_pb2.py' | xargs -I{} perl -pi -e 's|from cosmos.proto import|from x.cosmos_proto import|g' {}
find "$OUT_DIR" -name '*.py' | xargs -I{} perl -pi -e 's|from cosmos.|from x.cosmos.|g' {}
find "$OUT_DIR" -name '*.py' | xargs -I{} perl -pi -e 's|from tendermint.|from x.tendermint.|g' {}
find "$OUT_DIR" -name '*.py' | xargs -I{} perl -pi -e 's|from fx.|from x.fx.|g' {}
find "$OUT_DIR" -name '*_pb2.py' | xargs -I{} perl -pi -e 's|from google.api import|from x.google.api import|g' {}