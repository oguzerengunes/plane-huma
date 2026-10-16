# 08 — Go/No-Go Kurulum + İzin Testi

Tag kilit: `latest` yok, örn `v1.3.0`.
`curl -fsSL -o setup.sh .../releases/download/v1.3.0/setup.sh && ./setup.sh` → plane-app/docker-compose.yaml + plane.env üretir.

plane.env kritik: DATABASE_URL, REDIS_URL, AMQP_URL, WEB_URL, SECRET_KEY (openssl rand -hex 32), USE_MINIO=1 + MINIO_*.
Servisler: proxy, web, space, admin, api, worker, beat, live, pgdb, redis, rabbitmq, minio.
Kaynak kontrol: nproc>=2, RAM>=4GB (üretim 8GB). `docker compose ps` hepsi Up + `/api/healthz` 200.

İlk Owner: web'den ilk kayıt olan Owner olur. A (Bozok) workspace huma kur, B (Alkanat) Guest davet et. God-mode'dan SMTP + signup kısıtı.

## Test iskeleti (A=Member, B=Guest, PRIV=SECRET, PUB=PUBLIC)

- T1 login: POST /api/v1/sign-in/ → 200 token
- T2 private detay B: GET /workspaces/huma/projects/PRIV/ + Bearer B → 403/404 PASS
- T3 üye listesi B: GET .../project-members/ → 403/404
- T4 public self-join A: POST .../PUB/join/ → 200 role=Contributor
- T5 Guest self-join B: POST .../PUB/join/ → 400/403 RED PASS
- T6 Contributor davet edemez: POST .../invite/ + A_token → 403
- T7 issue: POST .../PRIV/issues/ + B → 403, POST .../PUB/issues/ + A → 201
- T8 MinIO presign: POST .../attachments/presign/ + A → 200 + PUT/GET 200

Kayıt: `deploy/go-no-go-test.sh` çalıştır, çıktıyı tabloya işle. Kritik FAIL (T2,T5,T6,T7) >=1 ise No-Go.

No-Go → Plan B: izolasyon kırılırsa / OOM sürekli / MinIO+SMTP 1 günde çözülmezse Vikunja'ya geç.
