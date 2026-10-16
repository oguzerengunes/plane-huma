# 10 — Hafta2-3 Davet Kodu + Duyuru/Intake

## huma_policy iskeleti (kod değil, dosya listesi)

- models.py: DepartmentInviteCode + DepartmentJoinRequest + UNIQUE/CHECK/index (detay backend-spec/schema.sql).
- serializers.py: Create (ttl 1-720, max 1-500) → expires_at, Response (plaintext bir kez), List (hash asla yok).
- views.py: 5 endpoint BaseAPIView, sıra JWT → workspace+project kapsam → permission → iş. Başka departman → 404.
- urls.py: `api/huma/` tek include, public/v1'e dokunma.
- adapter.py: `join(project_id,user_id)` → `ProjectMemberService.add_member(role=member)`. Direkt INSERT yasak.
- permissions: mevcut ProjectEntityPermission yeniden kullan, yeni yazma. Cache 5dk invalidate notu.
- migration: 0001 code, 0002 request, 0003 audit_reuse (tablo yok). code_hash SELECT service-role only.

Atomik: `UPDATE ... SET use_count+1 WHERE use_count<max_uses AND not revoked AND expires_at>now() RETURNING`. Yoksa jenerik 400. Approve: SELECT FOR UPDATE + join + approved tek transaction, çift karar 409.
Rate: IP+user+prefix 5/10dk → 429 + Retry-After. Başarılı sıfırlar. 3 IP aynı prefix → lidere uyarı. ip_hash 90 gün.
Audit: invite_code.created/revoked, join.requested/approved/rejected/failed_rate_limited. Plaintext hiçbir yerde yok.

## UI

/departman/katil: auto-uppercase + tire + paste, Katıl. 200→redirect, 202→bekliyor ekranı, hata tek tip, 429 ayrı.
/departman/:id/uyeler: kod tablosu (prefix, oluşturan, expiry, 3/50, onay, Kopyala/İptal), Yeni Kod modal (7gün, 50, onay toggle, plaintext bir kez), pending badge Realtime, Onayla/Reddet (double guard).
Bildirim: Realtime inbox+badge, Web Push (pending→lider, approve→üye, %80/expiry-24h→lider), Tauri native, e-posta approve/reject (kodsuz).

## Duyuru + Intake

Duyurular=PUBLIC proje, diğerleri PRIVATE. Yazma sadece Admin (başkan+1-2). Üyeler Commenter/Guest. Pages taslak→onay→Publish→pin. Private→Public çevirme yok.
Intake: Guest bile gönderir → lider Triage → Issue+assignee+Cycle. Gönderen backlog göremez. Yeni Intake→lidere, karar→talep edene bildirim.

Kabul: <2sn onaysız, pending'de önce satır yok sonra var, 6.deneme 429, revoke 400, dump'ta plaintext yok.
