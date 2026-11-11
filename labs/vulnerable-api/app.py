"""
Vulnerable REST API Target for Cyber Security Training Lab
Demonstrates key OWASP API Security Top 10 Vulnerabilities:
- API1: Broken Object Level Authorization (BOLA / IDOR)
- API2: Broken Authentication (Weak JWT, No Rate Limiting)
- API3: Broken Object Property Level Authorization (Mass Assignment)
- API4: Unrestricted Resource Consumption
- API5: Broken Function Level Authorization (BFLA)
- API7: Server-Side Request Forgery (SSRF)
- API8: Security Misconfiguration (Debug endpoints, stack traces)
"""

import os
import sys
import json
import jwt
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
JWT_SECRET = "supersecret_insecure_key_12345"  # Intentionally weak secret

# In-memory mock database
USERS = {
    1: {"id": 1, "username": "alice", "role": "user", "email": "alice@corp.local", "balance": 1500, "is_admin": False},
    2: {"id": 2, "username": "bob", "role": "user", "email": "bob@corp.local", "balance": 250, "is_admin": False},
    3: {"id": 3, "username": "admin_root", "role": "administrator", "email": "admin@corp.local", "balance": 999999, "is_admin": True},
}

ORDERS = {
    101: {"order_id": 101, "user_id": 1, "item": "Firewall License Tier 1", "amount": 500, "status": "shipped"},
    102: {"order_id": 102, "user_id": 2, "item": "Penetration Testing Toolkit", "amount": 1200, "status": "processing"},
    103: {"order_id": 103, "user_id": 3, "item": "C2 Infrastructure Dedicated Host", "amount": 8000, "status": "completed"},
}

def decode_token():
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        return None
    token = auth_header.split(" ")[1]
    try:
        # Intentionally vulnerable to algorithm confusion / none algorithm if token crafted
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256", "none"], options={"verify_signature": False} if "none" in token else {})
        return payload
    except Exception:
        return None

@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "service": "Cybersecurity Training Vulnerable API Target",
        "version": "1.0.0",
        "endpoints": [
            "POST /api/v1/auth/login",
            "GET  /api/v1/users/<id> (BOLA/IDOR)",
            "PUT  /api/v1/users/<id> (Mass Assignment)",
            "GET  /api/v1/orders/<order_id> (BOLA/IDOR)",
            "GET  /api/v1/admin/users (BFLA)",
            "POST /api/v1/admin/users (BFLA)",
            "POST /api/v1/tools/fetch_url (SSRF)",
            "GET  /api/v1/debug/env (Security Misconfiguration)"
        ]
    })

# API2: Broken Authentication
@app.route("/api/v1/auth/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}
    username = data.get("username", "")
    password = data.get("password", "")

    # Insecure mock auth: password is simply username + '123'
    for u_id, user in USERS.items():
        if user["username"] == username and password == f"{username}123":
            token = jwt.encode({"user_id": u_id, "username": username, "role": user["role"]}, JWT_SECRET, algorithm="HS256")
            return jsonify({"status": "success", "token": token, "user": user})

    return jsonify({"error": "Invalid username or password"}), 401

# API1: Broken Object Level Authorization (BOLA)
@app.route("/api/v1/users/<int:user_id>", methods=["GET"])
def get_user_profile(user_id):
    # Vulnerability: Does not verify whether token user_id matches requested user_id
    user = USERS.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

# API3: Broken Object Property Level Authorization (Mass Assignment)
@app.route("/api/v1/users/<int:user_id>", methods=["PUT"])
def update_user_profile(user_id):
    user = USERS.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json(silent=True) or {}
    # Vulnerability: Blindly accepts is_admin and role from user payload
    for k, v in data.items():
        user[k] = v
    return jsonify({"status": "updated", "user": user})

# API1: BOLA on Orders
@app.route("/api/v1/orders/<int:order_id>", methods=["GET"])
def get_order(order_id):
    order = ORDERS.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    return jsonify(order)

# API5: Broken Function Level Authorization (BFLA)
@app.route("/api/v1/admin/users", methods=["GET"])
def admin_list_users():
    # Vulnerability: Missing server-side role check, anyone with or without token can query
    return jsonify({"total_users": len(USERS), "users": list(USERS.values())})

# API7: Server-Side Request Forgery (SSRF)
@app.route("/api/v1/tools/fetch_url", methods=["POST"])
def fetch_url():
    data = request.get_json(silent=True) or {}
    url = data.get("url", "")
    if not url:
        return jsonify({"error": "Missing 'url' parameter"}), 400

    try:
        # Vulnerability: Directly queries arbitrary user-supplied URL without allowlist or loopback check
        resp = requests.get(url, timeout=3)
        return jsonify({"status": resp.status_code, "body": resp.text[:1000]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API8: Security Misconfiguration
@app.route("/api/v1/debug/env", methods=["GET"])
def debug_env():
    # Vulnerability: Exposes environment variables and JWT secret
    return jsonify({
        "debug": True,
        "environment": dict(os.environ),
        "jwt_secret_hint": JWT_SECRET,
        "python_version": sys.version
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
