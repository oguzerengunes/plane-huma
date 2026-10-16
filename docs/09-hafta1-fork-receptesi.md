# 09 — Hafta1 Fork Reçetesi

Fork: `makeplane/plane` → org `kulup-org/plane-huma` Public. Stable tag'den `huma/main`. Upstream remote ekle, preview takip etme.
Koru: LICENSE.txt + COPYRIGHT.txt, Commercial dizini. README'ye `Upstream: makeplane/plane@<tag>` + AGPL ibaresi.
Yama: tek commit `H-xxx:`, PATCHES.md satırı. H-000 applied, H-002..H-005 Hafta1'de applied olacak.
Rebase: 2 haftada diff, ayda rebase + duman testi. Dokunma: models/*, docker-compose.yml, .env.example, pnpm-lock, i18n/en/*.

Dev: upstream compose'a dokunma. `deploy/docker-compose.override.yml.example` → .yml, `.env.huma.example` → .huma. Komut: `docker compose -f docker-compose.yaml -f ../deploy/docker-compose.override.yml up -d`.

.env.huma: HUMA_PLANE_URL (=WEB_URL), HUMA_SOURCE_LINK, HUMA_DEPLOY_TAG, HUMA_ALLOWED_DOMAINS, HUMA_ENABLE_SIGNUP=0, HUMA_DEFAULT_PROJECT_NETWORK=SECRET, BACKUP_*.

God-mode: signup without invite OFF, workspace-creation restrict ON, Let members create projects OFF, SMTP kur, iç ağa kapat (#7167).

Markalama: apps/web/public logo/favicon, packages/ui logo bileşeni → apps/web/huma wrapper, tailwind token, i18n tr default + huma.json, footer Kaynak Kodu + tag/hash. Kontrol: `grep -r Plane apps/web/public packages/ui`.

Roller: Başkan Owner 1-2 (bypass var), lider Project Admin, üye Member+Contributor, mentor Guest+Commenter. Default SECRET: serializer default + dialog toggle gizle + publish Owner'a.

Mail kısıtı: önce prosedürel (davet-only + göz kontrolü), sonra validator (signup+invite+OAuth, #779). Test: izinsiz 400, OAuth bypass yok.

Çıkış: fork canlı + H-002..H-005 applied + God-mode tikli + 06'daki 8 test yeşil.
