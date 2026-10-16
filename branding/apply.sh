#!/bin/sh
set -e
SRC=$(dirname "$0")
mkdir -p ../web-huma/public
cp "$SRC/logo.svg" ../web-huma/public/logo.svg
cp "$SRC/huma.json" ../web-huma/huma.json
echo "branding applied"
