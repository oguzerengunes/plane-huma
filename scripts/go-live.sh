#!/bin/bash
set -euo pipefail
TAG=${HUMA_DEPLOY_TAG:-v1.3.0}
docker compose pull
TAG=$TAG docker compose up -d
sleep 10
curl -sf http://localhost:3000/api/health || curl -sf http://localhost:3000/ 
echo "GO-LIVE OK:$TAG"
