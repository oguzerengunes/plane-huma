# Hüma Invite API Spec (`/api/huma/`)

Auth: session JWT zorunlu. Rol Plane `project_member` tablosundan.

| Metod + Path | Yetki | Req | Res |
|---|---|---|---|
| POST /api/huma/invite-codes/ | admin/leader | {project_id, ttl_hours 1-720, max_uses 1-500, require_approval} | 201 {code_plaintext BİR KEZ, code_id, prefix, expires_at} |
| DELETE /api/huma/invite-codes/:id/ | üreten lider veya admin (başka departman → 404) | - | 200 {is_revoked:true} |
| POST /api/huma/join-by-code/ | giriş yapmış herkes (5/10dk limit) | {code} | 200 {joined} / 202 {pending, request_id} / 400 jenerik / 409 zaten üye / 429 limit |
| GET /api/huma/projects/:id/join-requests | admin/leader | ?status=pending | 200 [{request_id, user, created_at, prefix}] |
| POST /api/huma/join-requests/:id/approve | admin/leader | {} | 200 {approved} + üyelik oluşur |
| POST /api/huma/join-requests/:id/reject | admin/leader | {reason?} | 200 {rejected} |

Kurallar:
- Kod üretimi: `secrets.token_bytes(16)` → Base32-Crockford 26 char `HUMA-...` → `sha256` sakla, plaintext bir kez dön.
- Doğrulama: normalize (trim/upper/tire-sil) → sha256 → `hmac.compare_digest`. Hata tek tip.
- Approve: `SELECT FOR UPDATE` + `use_count < max_uses` + `adapter.join()` tek transaction.
- Adapter: `plane.services.ProjectMemberService.add_member(project_id, user_id, role=member)` yeniden kullan, direkt INSERT yok.
- Log: plaintext asla loglanmaz, `code_id + prefix + ip_hash` + 90 gün retention.
