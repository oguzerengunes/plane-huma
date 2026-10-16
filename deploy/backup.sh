#!/bin/sh
# Hüma yedekleme: Postgres dump + MinIO mirror (günlük cron/sidecar'dan çağrılır)
set -eu
DATE=$(date +%F)
BACKUP_DIR=${BACKUP_DIR:-/backups}
RETENTION=${HUMA_BACKUP_RETENTION_DAYS:-30}
echo "[huma-backup] $DATE dump başlıyor"
pg_dump -U "$POSTGRES_USER" -h db "$POSTGRES_DB" | gzip > "$BACKUP_DIR/plane-$DATE.sql.gz"
mc alias set huma "$HUMA_BACKUP_S3_ENDPOINT" "$MINIO_ROOT_USER" "$MINIO_ROOT_PASSWORD" >/dev/null
mc mirror "$BACKUP_DIR" "huma/$HUMA_BACKUP_BUCKET" --overwrite
find "$BACKUP_DIR" -name "plane-*.sql.gz" -mtime +"$RETENTION" -delete
echo "[huma-backup] tamam"
