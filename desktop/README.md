# Hüma Desktop (Tauri kabuk)

Plane web URL'sini saran ince kabuk. Ağır kod yok, iskelet.

- `tauri.conf.json.example` → `tauri.conf.json` kopyala, `HUMA_PLANE_URL` + `HUMA_UPDATER_PUBKEY` doldur.
- Pluginler: `tauri-plugin-notification` (yerel bildirim) + `tauri-plugin-updater` (otomatik güncelleme, imza zorunlu).
- Anahtar: `signer generate` → private key kasada + CI `TAURI_SIGNING_PRIVATE_KEY`, public `tauri.conf.json` içinde.
- Bildirim akışı: Web push → Tauri `sendNotification({title, body})`.
- Updater akışı: `check → downloadAndInstall → relaunch`, feed `latest.json` (GitHub Releases/S3).
- Boyut hedefi: ~5 MB, RAM düşük. Electron'a geçme.
