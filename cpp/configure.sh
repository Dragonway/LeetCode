#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$(readlink -f "$0")")"

cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug "$@"

echo
echo "[configure] OK"