#!/usr/bin/env python3
"""
FEZZY STATION — Production Flask App
Grant Fezzy Festers · Ravensmead · Cape Town · 2026
Deployed via Render · Strategy Over Impulse
"""

from flask import Flask, render_template_string, jsonify, request
import os
import socket
import logging
import subprocess
from datetime import datetime

app = Flask(__name__)

# ── Production Config ──
app.secret_key = os.environ.get("SECRET_KEY", "fezzy999bojack")
app.config["JSON_SORT_KEYS"] = False

# ── Logging Setup ──
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# ── HTML Path ──
HTML_PATH = os.path.join(os.path.dirname(__file__), "THE MAIN ONE.html")

def get_local_ip():
    """Get local IP address."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        logger.warning(f"Failed to get local IP: {e}")
        return "127.0.0.1"

@app.route("/")
def index():
    """Serve the main FEZZY STATION page."""
    try:
        with open(HTML_PATH, "r", encoding="utf-8") as f:
            html = f.read()
        logger.info("Served main page")
        return html
    except FileNotFoundError:
        logger.error("THE MAIN ONE.html not found")
        return """
        <div style="font-family:monospace;padding:40px;background:#0a0a0a;color:#ff69b4;text-align:center;">
            <h1 style="font-size:48px;">⚠️ FEZZY STATION</h1>
            <p style="font-size:20px;color:#00ffff;">THE MAIN ONE.html not found</p>
            <p style="color:#888;">Place it in the same directory as app.py</p>
            <p style="margin-top:30px;color:#ff1493;">Strategy Over Impulse · Grant Fezzy Festers · 999</p>
        </div>
        """, 404

# ── COMMAND BRIDGE ── (UPGRADED)
@app.route("/api/run", methods=["POST"])
def run():
    """Execute a shell command and return output — Fezzy OS Command Bridge."""
    cmd = request.json.get("cmd", "").strip()
    if not cmd:
        return jsonify({"status": "error", "output": "No command provided"})

    # Block dangerous commands
    blocked = ["rm -rf /", "mkfs", "dd if=", ":(){:|:&};:"]
    for b in blocked:
        if b in cmd:
            logger.warning(f"Blocked dangerous command: {cmd}")
            return jsonify({"status": "error", "output": "❌ Command blocked for safety"})

    try:
        logger.info(f"Running command: {cmd}")
        output = subprocess.getoutput(cmd)
        return jsonify({"status": "ok", "output": output or "(no output)"})
    except Exception as e:
        logger.error(f"Command error: {e}")
        return jsonify({"status": "error", "output": str(e)})

@app.route("/api/ip")
def api_ip():
    """Return IP info — used by the IP nav button."""
    import urllib.request
    try:
        external = urllib.request.urlopen("https://api.ipify.org", timeout=5).read().decode()
    except Exception as e:
        logger.warning(f"Failed to get external IP: {e}")
        external = "unavailable"

    return jsonify({
        "local": get_local_ip(),
        "external": external,
        "host": socket.gethostname(),
        "timestamp": datetime.utcnow().isoformat()
    })

@app.route("/api/status")
def api_status():
    """Health check endpoint for Render monitoring."""
    return jsonify({
        "status": "online",
        "brand": "FEZZY STATION",
        "operator": "Grant Fezzy Festers",
        "codename": "Bojack Fezzy 999",
        "location": "Ravensmead, Cape Town, South Africa",
        "timestamp": datetime.utcnow().isoformat(),
        "environment": os.environ.get("RENDER", "local")
    })

@app.route("/health")
def health():
    """Simple health check for Render."""
    return "OK", 200

@app.errorhandler(404)
def not_found(e):
    return jsonify({
        "error": "Not Found",
        "message": "This endpoint doesn't exist in FEZZY STATION",
        "brand": "Strategy Over Impulse"
    }), 404

@app.errorhandler(500)
def internal_error(e):
    logger.error(f"Internal error: {e}")
    return jsonify({
        "error": "Internal Server Error",
        "message": "Something went wrong in FEZZY STATION",
        "brand": "Strategy Over Impulse"
    }), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    local_ip = get_local_ip()

    print()
    print("  ╔═══════════════════════════════════════════╗")
    print("  ║    FEZZY STATION — Flask Server           ║")
    print("  ║    Grant Fezzy Festers · Bojack 999       ║")
    print("  ╠═══════════════════════════════════════════╣")
    print(f"  ║  Local   →  http://127.0.0.1:{port}         ║")
    print(f"  ║  Network →  http://{local_ip}:{port}  ║")
    print("  ║  Command Bridge → /api/run  ✅             ║")
    print("  ║  Press Ctrl+C to stop                     ║")
    print("  ╚═══════════════════════════════════════════╝")
    print()

    logger.info("FEZZY STATION starting up — Command Bridge ACTIVE")
    app.run(host="0.0.0.0", port=port, debug=False)
