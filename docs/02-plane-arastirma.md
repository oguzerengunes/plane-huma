# 02 — Plane CE Araştırma (DeepSeek v4.1 Flash kolu)

## Roller (2026 güncel adlar)

Workspace: Owner (her şey + silme/transfer, tüm projelere bypass) / Admin (ücretli, silme hariç aynı) / Member (sadece eklendiği projeyi görür, public'e self-join → Contributor olur) / Guest (sadece eklendiği proje, public'e self-join yok).

Proje: Admin (ayar + üye yönetimi + silme) / Contributor (yarat+düzenle, silme sadece kendi yarattığında) / Commenter (gör + yorum, yaratma yok) / Guest (sadece Intake gönderir).

Kritik:
- Değerlendirme: proje rolü → teamspace → workspace. Owner/Admin bypass projeden çıkarınca bile görür.
- Guest'e sadece Guest/Commenter verilebilir.
- Auto-join: Owner→Admin, Member→Contributor, Guest→katılamaz.
- Kendi rolünden üstünü yönetemezsin, son proje Admin'i ayrılamaz. İzin cache 5 dk.

## Public vs Private

- Public: tüm Member keşfeder + self-join. Guest göremez.
- Private: sadece davetliler + Owner/Admin (üyeliksiz görür).
- Private'a üye ekleme: sadece **Project Admin**.
- Public↔Private değişimi anında; Private→Public geri alınamaz görünürlük yaratır.

## Self-hosting

Servisler: web + space + admin (Next.js) + live (Yjs WS) + api (Django) + worker/beat (Celery) + migrator + proxy (Caddy) + monitor + silo + intake. Veri: Postgres 15.7+/16 + Redis/Valkey + RabbitMQ + MinIO + (opsiyonel OpenSearch).

Min: 2 CPU / 4 GB RAM, öneri 8 GB. `setup.sh` → `plane-app/docker-compose.yaml` + `plane.env`. Kritik env: DATABASE_URL, REDIS_URL, AMQP_URL, WEB_URL/APP_DOMAIN/CORS, SECRET_KEY, USE_MINIO.

## Django'ya modül ekleme (en temiz nokta)

`apps/api/plane/urls.py`: `api/` → plane.app.urls, `api/public/` → plane.space.urls, `api/v1/` → plane.api.urls.
Desen: Model → `plane/db/models/`, Serializer → `plane/api/serializers/`, View → `plane/api/views/<modül>.py` (BaseAPIView + `plane/app/permissions.py` ProjectEntityPermission kullan), URL → `plane/api/urls/<modül>.py`, async → `plane/bgtasks/`. Her sorguda workspace+project kapsamı zorunlu.

Kaynaklar: docs.plane.so/roles-and-permissions/overview, .../member-roles, .../permissions-matrix, core-concepts/projects/overview, .../manage-project-members, developers.plane.so/self-hosting/*
