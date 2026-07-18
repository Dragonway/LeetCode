#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$(readlink -f "$0")")"

usage() {
    echo "Usage:"
    echo "  ./test.sh <problem_name>    - build and run tests for a particular problem"
    echo "  ./test.sh --all             - build and run ALL tests"
    exit 1
}

[[ $# -ge 1 ]] || usage

if [[ ! -f build/CMakeCache.txt ]]; then
    echo "[test] Build dir not configured, running configure..."
    ./configure.sh
fi

if [[ "$1" == "--all" ]]; then
    echo "[test] Building all targets..."
    cmake --build build --config Debug
    echo "[test] Running ALL tests"
    ctest --test-dir build -C Debug --output-on-failure
else
    problem="$1"
    echo "[test] Building target: ${problem}"
    if ! cmake --build build --config Debug --target "${problem}"; then
        echo "[test] Build FAILED for target '${problem}'"
        exit 1
    fi

    echo "[test] Running tests for '${problem}'"
    ctest --test-dir build -C Debug -R "^${problem}\$" --output-on-failure
fi