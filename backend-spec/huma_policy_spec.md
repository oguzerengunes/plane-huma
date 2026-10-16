# huma_policy iskeleti (spec, kod değil)

Dosyalar: __init__.py (marker), models.py (DepartmentInviteCode + DepartmentJoinRequest, UNIQUE(code_id,user_id)), serializers.py (InviteCreate ttl 1-720 max 1-500, JoinByCode tek alan, JoinDecision reason opsiyonel), views.py (üret→katıl→listele→onayla→reddet), urls.py (POST invite-codes/, POST join-by-code/, GET projects/:id/join-requests, POST approve/reject), adapter.py join(project_id,user_id) → add_member(role=member), tests.md 5 kabul.

UI /departman/katil: input HUMA-XXXX + Katıl (disable+spinner, 429'da geri sayım). 3 dal: joined→redirect, pending→bilgi kartı, hata tek tip.
UI /departman/:id/uyeler: Üye/Tarih/Badge/İşlem tablosu, İncele modal (prefix only), pending rozeti.

Güvenlik: 26-char secrets.token_bytes(16) Base32, sha256 + compare_digest, 5/10dk 429 + Retry-After, audit code_id+prefix+ip_hash 90gün, başka departman 404, atomik WHERE use_count<max_uses + SELECT FOR UPDATE.
