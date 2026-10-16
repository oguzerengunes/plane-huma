# PATCHES — Hüma fork yama listesi

| ID | Tarih | Tag Baz | Dosya | Neden | Upstream Issue | Rebase Durumu |
|---|---|---|---|---|---|---|
| H-000 | 2026-10-16 | v1.3.0 | (yok) | Repo iskeleti: docs/deploy/desktop/backend-spec | - | applied/clean |
| H-001 | 2026-10-16 | v1.3.0 | apps/api/huma_policy/* | Davet kodu + lider onayı (models/utils/serializers/views/urls/adapter/validators/migration) | - | applied/clean |
| H-002 | 2026-10-16 | v1.3.0 | apps/web/huma/* | Markalama + JoinByCode + InviteCodePanel + footer (branding/logo.svg, huma.json) | - | applied/clean |
| H-003 | 2026-10-16 | v1.3.0 | packages/i18n/src/locales/tr/* | huma.json TR namespace | #6922 | applied/clean |
| H-004 | 2026-10-16 | v1.3.0 | apps/api signup validator | validators.py üni domain kısıtı | #779 | applied/clean |
| H-005 | 2026-10-16 | v1.3.0 | project serializer | default_secret.py SECRET + Owner-only | - | applied/clean |
| H-006 | 2026-10-16 | v1.3.0 | scripts/fork-setup.sh + plane_integration/ | Fork pin + settings/urls snippet | - | applied/clean |

Kural: tek yama = tek commit, mesaj `H-xxx: <açıklama>`.
