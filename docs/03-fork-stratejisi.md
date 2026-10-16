# 03 — Fork Stratejisi + AGPL + Markalama

## AGPL-3.0

- Fork public: `kulup-org/plane-huma` (`preview`'dan değil stable tag'den).
- LICENSE.txt + COPYRIGHT.txt silinmez, üstüne kulüp notu.
- AGPL §13: ağdan sunuyorsan kaynak linki arayüzde görünür olmalı → footer `Kaynak Kodu (AGPL)` + tag/commit hash.
- Marka: Plane adı/logo/favicon/e-posta şablonları → Hüma. README'ye `Upstream: makeplane/plane@<tag>` yaz.
- Commercial koda dokunma, lisans değiştirme, kaynak linkini gizleme.

## Değiştir / Değiştirme

- DEĞİŞTİRME: `apps/api/plane/db/models/*`, `docker-compose.yml`, `.env.example`, `pnpm-lock.yaml`, `packages/i18n/.../en/*`, LICENSE.
- DEĞİŞTİR (ince): `docker-compose.override.yml`, `.env.huma.example`, `deployments/huma/*`, `apps/api/huma_policy/*` (yeni app), `apps/web/huma/*`, `packages/i18n/.../tr/*`.
- Rebase: `preview` takip edilmez, stable tag'e kilitlen. 2 haftada diff, ayda bir rebase + duman testi.

## Markalama

Logo: `apps/web/public/*`, `packages/ui/*logo*`, login/header/sidebar, God-mode, mail şablonları. Renk: `packages/tailwind-config/*` token'ları. Türkçe Nisan 2025'te geldi (`packages/i18n/.../tr/*.json`), default `tr` yap, marka kelimeleri ayrı `huma.json` namespace'te tut.

## Kayıt kısıtlama (3 kademe)

1. Sıfır kod: God-mode `Allow anyone to sign up without invite = OFF` + `ENABLE_SIGNUP=0` + `Prevent workspace creation = ON` + SMTP. Üni kontrolü prosedürel.
2. Az kod: signup/invite serializer'a `allowed_domains` validator (OAuth dahil, bypass testi şart).
3. Proxy: Caddy/Nginx'te `/auth/*` rate-limit. Tek başına yetmez, 1+2 ile birlikte.

God-mode'u iç ağa kapat (geçmiş bypass bug #7167).

## Proje oluşturma

Kod yazmadan %90: `Let members create projects = OFF` → sadece Owner/Admin açar. Başkanı Owner yap, herkesi Member/Guest. Default Private: serializer'da `network` default `SECRET` (ProjectNetwork SECRET=0, PUBLIC=2) + frontend dialog'da Public toggle gizle. Ek sertlik: publish yetkisini Owner'a indir.
