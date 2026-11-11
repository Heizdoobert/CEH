#!/usr/bin/env bash
# ==============================================================================
# SEC Lab Orchestration - Stop and Teardown Lab Containers
# ==============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${SCRIPT_DIR}"

echo "======================================================================"
echo "          Stopping CEH v12 & Red Team Hands-on Lab Environment        "
echo "======================================================================"

if docker compose version >/dev/null 2>&1; then
    COMPOSE_CMD="docker compose"
elif command -v docker-compose >/dev/null 2>&1; then
    COMPOSE_CMD="docker-compose"
else
    echo "[ERROR] docker compose or docker-compose is required."
    exit 1
fi

echo "[*] Stopping and removing lab containers..."
${COMPOSE_CMD} down

echo "[+] Lab environment teardown complete."
