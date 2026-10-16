# 05 — Masaüstü + Yedekleme + Plan B

## Tauri (öneri) vs Electron

Tauri 2.x: ~0.6-10 MB (WebView2/WKWebView), düşük RAM, Rust memory-safety + capability modeli, updater imzası zorunlu. Electron: 50-150 MB gömülü Chromium, yüksek RAM. Kulüp laptopları için **Tauri**.

Bildirim: `tauri-plugin-notification` (isPermissionGranted → request → sendNotification). Updater: `tauri-plugin-updater` + `tauri.conf.json > plugins.updater {pubkey, endpoints}` + `bundle.createUpdaterArtifacts:true`. Akış: `signer generate` → CI `TAURI_SIGNING_PRIVATE_KEY` → `.sig` + `latest.json` (GitHub Releases/S3) → `check → downloadAndInstall → relaunch`.

Yapı: `src-tauri/tauri.conf.json` (Plane URL + updater), `src-tauri/src/main.rs` (~20 satır: Builder + plugin init + pencere), `capabilities/default.json` (updater+notification izinleri), `icons/`. Detay: `desktop/README.md`.

## Yedekleme (Postgres + MinIO)

`backup` sidecar (postgres:18 + mc) veya host cron: `pg_dump | gzip > /backups/plane-%F.sql.gz` → `mc mirror /backups bucket --overwrite` → 7/30 gün rotasyon + MinIO lifecycle. Restore provası ayda 1 (`psql < yedek` + geri mirror). 20 GB plan: OS+imaj 6, Postgres 2-4, MinIO 4-6, /backups 4-6. %80 alarm.

## Duyurular

(a) Pages Publish → herkese açık salt-okunur link (nested dahil, yorum kapalı, Unpublish ile geri alınır, teamspace yayınlanamaz). (b) Public proje (salt-okunur). Öneri: Wiki'de yaz → Publish → linki Duyurular projesinde sabitle.

## Plan B — Vikunja

AGPL-3.0, Go+Vue, tek konteyner, SQLite/Postgres. Artı: hafif, yedek = dump + klasör. Eksi: Cycle/Module/roadmap/Pages/entegrasyon sığ, topluluk küçük. İzin: paylaşım başına rights int (0 read,1 write,2 admin) — Plane katmanlı matrise göre basit. Geçiş eşiği: Plane RAM/bakım yorarsa, ihtiyaç Kanban+duyuru ise, VPS limitine takılınırsa.

Elendi: Planka (tek pano, izin/analitik zayıf), Focalboard (arşivlendi/ölü).
