# Hüma Desktop BUILD (10 adım)
1. conf: example → tauri.conf.json, HUMA_PLANE_URL yaz.
2. ikon: icons/icon.png koy, productName Hüma, id tr.edu.kulup.huma.
3. signer: `pnpm tauri signer generate -w ~/.tauri/huma.key`, .pubkey al.
4. pubkey: plugins.updater.pubkey + endpoints düzelt.
5. CI: TAURI_SIGNING_PRIVATE_KEY + PASSWORD ekle.
6. build: `pnpm tauri build`.
7. .sig: bundle altında .sig var mı bak.
8. latest.json: version+url+signature, releases/latest/download yoluna koy.
9. release: exe + .sig + latest.json yükle.
10. kurulu test: temiz VM kur + login + güncelleme doğrula.
