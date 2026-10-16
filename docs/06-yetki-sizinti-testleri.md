# 06 — Yetki Sızıntı Testleri (yayından önce şart)

Her biri üye-olmayan kullanıcı ile dene. Biri patlarsa yayın yok.

1. Proje listesi/arama: A ile giriş → üye olunmayan proje adı arat → sonuç boş olmalı.
2. Direkt URL: A'nın `/projects/<id>/issues/<id>` linkini B aç → 403/404, veri yok.
3. API token: `curl -H "Authorization: Bearer <B-token>" /api/v1/projects/<A-id>/` → 403. Token iptalinde kesilmeli.
4. Workspace view/analitik: Viewer `/analytics/` aç + API çağır → sadece yetkili workspace.
5. MinIO linkleri: A dosyasının imzalı URL'sini B (inkognito) aç → red. Süre dolunca tekrar dene → red. `mc ls` public bucket yok.
6. Bildirim/e-posta: ilgisiz issue yorumu B'ye gitmemeli (posta + inbox kontrol).
7. IDOR: proje ID ±1, UUID varyasyon → hepsi 403/404.
8. Çıkarılan üye: A'yı çıkar → eski sekme refresh + eski token → ikisi de red, cache'ten veri yok.
9. Davet kodu: DB dump'ta plaintext yok, 6. yanlışta 429, revoke sonrası 400, tek tip hata mesajı.
10. Owner bypass doğrulama: projeden çıkarılan Owner yine görür (tasarım), Member görmez. Owner sayısı 1-2 mi?

Kayıt: tarih, test eden, sonuç (geçti/kaldı), bulgu issue linki.
