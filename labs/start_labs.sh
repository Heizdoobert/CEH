#!/usr/bin/env bash
# ==============================================================================
# SEC Lab Orchestration - Start All Lab Containers
# ==============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${SCRIPT_DIR}"

echo "======================================================================"
echo "          Starting CEH v12 & Red Team Hands-on Lab Environment        "
echo "======================================================================"

# Check Docker prerequisite
if ! command -v docker >/dev/null 2>&1; then
    echo "[ERROR] Docker is not installed or not in PATH."
    exit 1
fi

# Detect docker compose syntax
if docker compose version >/dev/null 2>&1; then
    COMPOSE_CMD="docker compose"
elif command -v docker-compose >/dev/null 2>&1; then
    COMPOSE_CMD="docker-compose"
else
    echo "[ERROR] docker compose or docker-compose is required."
    exit 1
fi

echo "[*] Verifying lab configuration..."
python3 "${SCRIPT_DIR}/scripts/verify_lab_config.py"

echo "[*] Starting lab containers with ${COMPOSE_CMD}..."
${COMPOSE_CMD} up -d

echo ""
echo "======================================================================"
echo "                   Lab Targets Ready & Accessible                     "
echo "======================================================================"
echo " 1. DVWA (Damn Vulnerable Web App) : http://localhost:8080 (172.28.0.10)"
echo "    Default login: admin / password"
echo " 2. OWASP Juice Shop               : http://localhost:3000 (172.28.0.20)"
echo " 3. Vulnerable REST API (OWASP)    : http://localhost:5000 (172.28.0.30)"
echo "    Endpoints: /api/v1/auth/login, /api/v1/users/{id}, /api/v1/admin/debug"
echo " 4. Metasploitable Linux Target    : Ports 2121(FTP), 2222(SSH), 8088(HTTP)"
echo " 5. Netshoot Sniffer Pod           : sec_lab_sniffer (Interactive Packet Analysis)"
echo "======================================================================"
echo "[+] Walkthroughs: See labs/README.md and labs/challenges/01_Hands_On_Lab_Flags_and_Walkthroughs.md"
