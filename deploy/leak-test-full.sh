#!/bin/bash
# 10 sızıntı testi — docs/06 ile birebir
set -u
B=${1:-http://localhost:3000}
T=${TOKEN:-test-token}
t() { code=$(curl -ks -o /dev/null -w %{http_code} -H "Authorization: Bearer $T" "$B$1"); echo "$code $2"; }
t "/api/v1/projects/PRIV/" "1-direkt-URL"
t "/api/v1/projects/PRIV/members/" "2-uye-listesi"
t "/api/v1/analytics/" "3-analitik"
t "/api/v1/search?q=PRIV" "4-arama"
t "/api/v1/attachments/signed/" "5-minio"
t "/api/v1/notifications/" "6-bildirim"
t "/api/v1/projects/9999/" "7-idor"
t "/api/v1/projects/PRIV/issues/" "8-cikarilmis-uye"
t "/api/huma/join-by-code/" "9-davet-kodu"
t "/api/v1/projects/PRIV/" "10-owner-bypass"
