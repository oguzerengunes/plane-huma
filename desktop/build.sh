#!/bin/bash
set -e
pnpm tauri build
ls src-tauri/target/release/bundle/
echo "build tamam: $(date -u +%F)"
