# Fork Entegrasyonu (kopyala-yapıştır)

1. `backend-spec/huma_policy/` → `apps/api/huma_policy/` kopyala.
2. settings INSTALLED_APPS +1 satır.
3. ana urls.py +1 include.
4. migration üret + uygula + tablo doğrula (3 adım).
5. `web-huma/` → web app huma/ klasörüne kopyala.
6. footer Kaynak Kodu linki ekle.
7. i18n tr huma anahtarları ekle.
8. God-mode 4 ayar: signup OFF, workspace restrict ON, members create OFF, SMTP.

Dokunma: auth akışı, workspace/proje modelleri, issue/cycle mantığı, eski migration, compose, bağımlılık sürümleri.

Duman: migrate → up → login → join-by-code → approve. Hepsi yeşilse OK.

Rollback: huma klasör + settings/urls ekini geri al → son migration geri → restart + login kontrol.
