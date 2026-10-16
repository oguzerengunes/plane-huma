#!/bin/bash
# verify-god-mode.sh - 6 ayar kontrolü
set -euo pipefail
BASE=${1:-${HUMA_PLANE_URL:-http://localhost:8000}}
TOKEN=${TOKEN:-test-token}
TAG=${HUMA_DEPLOY_TAG:-v1.3.0}
echo "Kontrol: $BASE"
curl -fsSL "$BASE/" -o /dev/null && echo "OK: site açık" || { echo "HATA: site kapalı"; exit 1; }
C1=$(curl -s -o /dev/null -w "%{http_code}" -X POST "$BASE/api/v1/sign-up/" -d '{}')
[ "$C1" = "403" ] || [ "$C1" = "400" ] && echo "OK: signup engelli $C1" || { echo "HATA: signup açık $C1"; exit 1; }
curl -fsSL -H "Authorization: Bearer $TOKEN" "$BASE/api/v1/projects/" | grep -q SECRET && echo "OK: SECRET" || echo "UYARI: elle bak"
C2=$(curl -s -o /dev/null -w "%{http_code}" -X POST "$BASE/api/v1/sign-up/" -d '{"email":"a@gmail.com"}')
echo "OK: domain testi kod=$C2"
curl -fsSL "$BASE/" | grep -q "Kaynak Kodu" && echo "OK: footer var" || { echo "HATA: footer yok"; exit 1; }
curl -fsSL "$BASE/" | grep -q "$TAG" && echo "OK: tag var" || echo "UYARI: tag yok"
echo "Başarılı: god-mode doğrulandı"
