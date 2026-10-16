# 11 — Hafta4 Masaüstü + Yedek + Pilot

Tauri: example→tauri.conf.json, productName Hüma, id tr.edu.kulup.huma, version senkron, windows.url=HUMA_PLANE_URL 1280x800. Updater active+pubkey string+https endpoints+createUpdaterArtifacts true. Capabilities: updater:default/check/download-install + notification:default + dialog + process:restart. signer generate -w ~/.tauri/huma.key 0600, private kasada, CI TAURI_SIGNING_PRIVATE_KEY. Build çıktısında .sig var mı, latest.json (version, notes, pub_date RFC3339, platforms.windows.signature=url) Release'e yükle, kurulu exe'de check→install→relaunch dene. Bildirim: granted→request→send, ilk açılışta bir kez. WebView2 kontrol.

Yedek: sidecar veya cron. pg_dump|gzip → mc mirror --overwrite. 7 gün + 1 aylık (RETENTION=30). df -h 20GB plan (6+4+6+6). %80 alarm (cron+webhook). mc ilm lifecycle. Ayda 1 restore provası (boş DB psql + mirror geri + login testi), logla.

Sızıntı final: 06'daki 10 madde PASS/FAIL tablosu (eden+tarih+issue). MinIO private, çıkarılan üye 3x RED, kod 429/400/plaintext yok, Owner 1-2. Biri FAIL → yayın yok.

Bozok pilotu 2 hafta: sadece Bozok PRIVATE (KTR/Telemetri/Gövde). Kriter: aktif ≥%60, sprint ≥%70 closed, kod sayıları + 0 sızıntı + 0 kayıp. Form 5 soru: kolaylık 1-5, davet akışı, aksayan, Tauri OS, açılsın mı. Link Duyurularda sabit, rapor yaz.

Karar: YEŞİL açıl (10 PASS + hedef + ≥%70 onay), SARI 1 hafta uzat, KIRMIZI durdur → Vikunja.

Devamlılık: docs güncel, rol devri (Owner/backup/lider+ yedek isim), repo org'da + footer link, tag pin + latest.json eşleşme, secret kasada, cron takvimi devredildi.
