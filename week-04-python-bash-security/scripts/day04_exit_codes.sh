#!/usr/bin/env bash
# Exit codes: 0 = success, non-zero = failure. $? holds the last exit code.

target="${1:-/etc/hostname}"      # first argument, with a default

if [ -e "$target" ]; then
    echo "Found: $target"
    exit 0
else
    echo "Missing: $target" >&2
    exit 1
fi
