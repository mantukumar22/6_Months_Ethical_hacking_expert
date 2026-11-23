#!/usr/bin/env bash
set -e
names=(computer-architecture resource-baseline security-layers os-enumeration process-analysis filesystem-security system-baseline-report)
out=../cyber-repos
mkdir -p "$out"
for i in 1 2 3 4 5 6 7; do
  n=$(printf "%02d" $i)
  dest="$out/cyber-$n-${names[$((i-1))]}"
  mkdir -p "$dest"
  cp -r "day-$n"/. "$dest"/
  cp .gitignore "$dest"/
  (cd "$dest" && git init -q && git add . && git commit -qm "Day $n: initial commit" && echo "Created $dest")
done
