#!/usr/bin/env bash

for item in pwd whoami date
do
    echo "Running: $item"
    "$item"
    echo
done
