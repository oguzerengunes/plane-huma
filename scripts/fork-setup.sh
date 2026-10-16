#!/bin/bash
# Fork kurulum: upstream + stable tag + huma/main (çalıştırınca yapar)
set -euo pipefail
TAG=${HUMA_DEPLOY_TAG:-v1.3.0}
git remote add upstream https://github.com/makeplane/plane.git 2>/dev/null || true
git fetch upstream --tags
git checkout -B huma/main "$TAG" 2>/dev/null || git checkout -B huma/main
test -f LICENSE.txt || test -f LICENSE || echo "UYARI: LICENSE eksik!"
echo "OK: huma/main baz=$TAG"
