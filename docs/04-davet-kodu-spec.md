# 04 — Davet Kodu + Lider Onayı Spec (kod yok, spec var)

## Tablolar

`department_invite_code(id, project_id, code_hash CHAR64 UNIQUE, code_prefix CHAR4, created_by, expires_at, max_uses, use_count, require_approval BOOL, is_revoked BOOL, created_at, revoked_at)` + index (project, expiry) where not revoked.

`department_join_request(id, code_id FK CASCADE, project_id denormalize, user_id, status pending/approved/rejected, decided_by, decided_at, created_at, UNIQUE(code_id,user_id))` + index pending + user.

Audit için yeni tablo açma: mevcut `project_activity` / `audit_log(event, actor_id, project_id, metadata JSONB)` kullan. Event: invite_code.created/revoked, join.requested/approved/rejected/failed_rate_limited. Plaintext kod ASLA loglanmaz (code_id + prefix + ip_hash).

Neden hash: dump sızsa kullanılamaz, lider bile göremez (sadece prefix), doğrulama `hmac.compare_digest(sha256(gelen), stored)`. Neden rate-limit: brute-force + enumeration oracle + DoS koruması.

## API (`/api/huma/`, JWT zorunlu)

- `POST /api/huma/invite-codes/` — sadece admin/leader. Req `{project_id, ttl_hours 1-720, max_uses 1-500, require_approval}`. Res `201 {code_plaintext BİR KEZ, code_id, prefix, expires_at}`.
- `DELETE /api/huma/invite-codes/:id/` — üreten lider veya admin. Başka departman → 404 (403 değil, bilgi sızdırmamak için).
- `POST /api/huma/join-by-code/` — giriş yapmış herkes. Req `{code}` normalize (trim/upper/tire-sil). Res `200 {joined}` veya `202 {pending, request_id}`. Hata tek tip: `Kod geçersiz veya süresi dolmuş`. Limit aşımı 429 + Retry-After.
- `GET /api/huma/projects/:id/join-requests?status=pending` — sadece admin/leader.
- `POST /api/huma/join-requests/:id/approve` / `reject` — sadece admin/leader, çift karar 409. Approve tek transaction: `SELECT FOR UPDATE` + `use_count < max_uses` + adapter.join + status update.

E3 sırası: rate-limit → hash lookup → revoke/expire/kontenjan (jenerik 400) → zaten üye 409 → require_approval FALSE ise adapter.join + atomik `use_count++` → TRUE ise pending yaz.

## Güvenlik

- Kod: `secrets.token_bytes(16)` 128-bit. Base32-Crockford tireli `HUMA-XXXX-...`. Not: 16 char=80bit, 20 char=100bit; gerçek 128-bit için **26 char (130bit)**. Tavsiye 26 char + kopyala butonu. Hash SHA-256 saltsız (128-bit rastgele, rainbow anlamsız).
- Limit: IP+user 5 başarısız/10 dk, başarılı sıfırlar, artan gecikme. 3 farklı IP aynı prefix → lidere uyarı.
- RLS: `code_hash` SELECT sadece service-role. KVKK: IP hash, 90 gün retention.

## UI

`/departman/katil`: kod kutusu (auto-uppercase, tire otomatik) + Paste + Katıl. Sonuç: joined → redirect, pending → `İsteğin lidere iletildi`, hata tek tip, 429 ayrı.
`/departman/:id/uyeler`: kod tablosu (prefix, oluşturan, expiry, 3/50, onay?, Kopyala/İptal) + Yeni Kod modal (süre default 7 gün, max, onay toggle) + Bekleyenler (avatar+ad+mail, tarih, prefix, Onayla/Reddet). Bildirim: Realtime INSERT → lidere push, approve/reject → üyeye push + Tauri notification + e-posta, expiry-24h veya %80 doluluk → lidere uyarı.

## Plane'e bağlanma (Adapter)

Direkt INSERT yapma (bildirim/activity bozulur). `huma_membership_adapter.join(project_id, user_id)` içinde tek satır `plane.services.ProjectMemberService.add_member(..., role=member)`. Dokunuş 2 yer: yeni `huma/` app + `adapter.py` (~15 satır). Race: `UPDATE ... SET use_count=use_count+1 WHERE id=:id AND use_count<max_uses RETURNING`.

Kabul: 26-char onaysız <2sn, onaylıda önce satır yok sonra var, 6. yanlışta 429, revoke sonrası 400, dump'ta plaintext yok.

Akış: Üye --join-by-code--> backend (rate/hash/revoke) --FALSE--> add_member --> joined. --TRUE--> pending --> Realtime lidere --> Onayla --> adapter.join --> push.
