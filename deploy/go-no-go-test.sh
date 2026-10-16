#!/bin/bash
# Go/No-Go iskeleti — gerçek token/ID'leri doldurup çalıştır. Beklenen: kritik FAIL=0 → Go.
set -u
WS="${WS:-huma}"
PRIV="${PRIV:-bozok-private-id}"
PUB="${PUB:-duyurular-public-id}"
API="${API:-http://localhost:3000}"
echo "== T1 login =="
# TOKEN_A=$(curl -s -X POST $API/api/v1/sign-in/ -H 'Content-Type: application/json' -d '{"email":"A","password":"..."}' | jq -r .token)
# TOKEN_B=...
echo "T2 private detay B → 403/404 bekle: curl -s -o /dev/null -w %{http_code} $API/api/v1/workspaces/$WS/projects/$PRIV/ -H \"Authorization: Bearer \$TOKEN_B\""
echo "T3 üye listesi B → 403/404"
echo "T4 public join A → 200 Contributor"
echo "T5 Guest join B → 400/403"
echo "T6 Contributor invite → 403"
echo "T7 PRIV issue B 403 / PUB issue A 201"
echo "T8 presign A 200"
echo "Sonuçları docs/06 tablosuna PASS/FAIL işle"
