#!/bin/bash
set -euo pipefail
DUMP=/var/backups/huma-$(date +%F).sql.gz
pg_dump -U huma humadb | gzip > "$DUMP"
[ "$(stat -c%s "$DUMP")" -gt 0 ] || { echo "DUMP BOŞ"; exit 1; }
gunzip -t "$DUMP" && echo "OK: $DUMP"
USE=$(df / | awk 'NR==2{print $5}' | tr -d %)
[ "$USE" -ge 80 ] && echo "ALARM: disk %$USE dolu"
ls -lh "$DUMP"
