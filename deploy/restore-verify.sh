#!/bin/bash
# restore-verify.sh - son yedeği test DB'ye yükle
set -euo pipefail
BACKUP_DIR=${BACKUP_DIR:-/backups}
TEST_DB=${TEST_DB:-plane_test}
DB_USER=${POSTGRES_USER:-postgres}
BASE=${HUMA_PLANE_URL:-http://localhost:8000}
LAST=$(ls -t "$BACKUP_DIR"/plane-*.sql.gz | head -n1)
echo "Bulundu: $LAST"
dropdb -U "$DB_USER" -h db --if-exists "$TEST_DB"
createdb -U "$DB_USER" -h db "$TEST_DB"
gunzip -c "$LAST" | psql -U "$DB_USER" -h db "$TEST_DB" >/dev/null
C1=$(psql -U "$DB_USER" -h db -t -c "SELECT COUNT(*) FROM project_project;" "$TEST_DB" | xargs)
C2=$(psql -U "$DB_USER" -h db -t -c "SELECT COUNT(*) FROM department_invite_code;" "$TEST_DB" | xargs)
C3=$(psql -U "$DB_USER" -h db -t -c "SELECT COUNT(*) FROM department_join_request;" "$TEST_DB" | xargs)
echo "project=$C1 invite=$C2 request=$C3"
[ "$C1" -eq 0 ] && { echo "HATA: tablo boş"; exit 1; }
echo "Başarılı: restore doğrulandı $LAST"
