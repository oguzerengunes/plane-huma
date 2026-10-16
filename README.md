# Hüma v2 — Fork Tabanlı Kulüp Proje Yönetim Uygulaması

> Taban: **Plane Community Edition (AGPL-3.0)** fork'u. Sıfırdan yazmak yok.
> Workspace = Kulüp, Departman = Private Project, Alt proje = Module, Sprint = Cycle.

## Hızlı karar

- Forum yazılımları elendi (görev/Kanban/atama yok).
- Departman = Plane'de **private proje**. Sadece davetle girilir.
- Bizim eklediğimiz ana özellik: **departman davet kodu + lider onayı** (Plane'de yok).
- Masaüstü: Plane web'i saran ince **Tauri kabuğu**.
- Plan B: **Vikunja** (hafif) veya Supabase sıfırdan.

## Repo yapısı

```
docs/                    # araştırma + kararlar (DeepSeek v4.1 Flash kolları)
  01-karar-ozeti.md .. 07-zaman-cizelgesi.md
  08-go-no-go-kurulum.md, 09-hafta1-fork-receptesi.md
  10-hafta2-3-implementasyon.md, 11-hafta4-pilot.md
  12-pilot-rollout.md, 13-yayin-kapisi.md, 14-entegrasyon.md
deploy/                  # docker override + env + yedekleme (upstream compose'a dokunma)
  go-no-go-test.sh, verify-god-mode.sh, restore-verify.sh, backup.sh
desktop/                 # Tauri kabuk (conf + Cargo + capabilities + BUILD)
  src-tauri/, src/main.js, package.json, BUILD.md
backend-spec/            # huma invite modülü (schema + api spec + huma_policy kodu)
  huma_policy/models.py, utils.py, serializers.py, adapter.py, views.py, urls.py
web-huma/                # davet kodu UI (JoinByCode + InviteCodePanel + api.js)
PATCHES.md               # fork yama listesi (H-xxx)
```

## Başlangıç (Gün 1-2 go/no-go)

1. `deploy/.env.huma.example` → `.env.huma` kopyala, `deploy/docker-compose.override.yml.example` incele.
2. Upstream Plane'i stable tag'e kilitle (örn. `v1.3.0`), `docker compose up` ile kaldır.
3. `docs/06-yetki-sizinti-testleri.md` içindeki 8 testi iki kullanıcı ile yap:
   Bozok üyesi Alkanat private projesini göremiyor mu?
4. Sonuç No-Go ise `docs/05-masaustu-yedekleme-planB.md` → Vikunja'ya geç.

## Roller

| Hüma | Plane |
|---|---|
| Kulüp Başkanı (+1 yedek) | Workspace Owner (sayıyı 1-2 tut, tüm private'ları görür) |
| Departman Lideri | Project Admin (üye ekler, kod üretir, onay verir) |
| Üye | Workspace Member + Project Contributor |
| Misafir/Mentor | Workspace Guest + Project Guest/Commenter |

## Fork kuralları

- Public fork: `kulup-org/plane-huma`, `LICENSE.txt` + `COPYRIGHT.txt` korunur.
- Upstream dosyayı değiştirme, `huma/` ayrı modül + `docker-compose.override.yml` kullan.
- Her yama tek commit `H-xxx:` + `PATCHES.md` satırı.
- Footer'a `Kaynak Kodu (AGPL)` linki + deploy tag/hash (AGPL §13).
- Marka: Plane logo/ismini kaldır → Hüma. `tr` locale default.

## Lisans

AGPL-3.0. Upstream: `makeplane/plane@<tag>`. Değişiklikler aynı lisansla açık.
