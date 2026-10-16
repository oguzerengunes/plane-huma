# Hüma — Katkı Rehberi

Branch: `huma/main` tek kaynak; feature: `huma/H-xxx-kısa-ad`.
Commit: `H-xxx: fiil + kısa açıklama`.
PR: küçük tut, H-xxx linkle, lint+test yeşil olmalı.
Rebase: PR öncesi `git fetch && git rebase origin/huma/main`. Force-push yok.
AGPL: Bu repo AGPL-3.0 Plane fork'udur; kapalı dağıtım yok. LICENSE korunur.
Yasak: `.env.huma`, `*.pem`, `*.sig`, plaintext kod commit'leme.
Review: 1 onay + CI yeşil olmadan merge yok. huma/main'e direkt push yasak.
Issue: H-xxx aç, kabul kriteri + pilot etkisi yaz.
