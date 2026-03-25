# FEZZY STATION — Flask Web Server

**Grant Fezzy Festers · Bojack Fezzy 999 · Strategy Over Impulse**  
**Location:** Ravensmead, Cape Town, South Africa

---

## 🎯 Overview

Production-ready Flask web server for FEZZY STATION. Built in Termux on Android 14 (Honor X5b / GFY-LX2P), deployed to Render for global access.

## 🚀 Features

- **Main Dashboard:** Serves THE_MAIN_ONE.html interface
- **IP API:** Returns local + external IP info
- **Status API:** Health monitoring endpoint
- **Production-Ready:** Logging, error handling, environment configs
- **Mobile-First:** Built entirely on Android via Termux

## 📋 Requirements

- Python 3.11+
- Flask 3.0.0
- Gunicorn 21.2.0

## 🔧 Local Setup (Termux)

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/fezzy-station.git
cd fezzy-station

# Install dependencies
pip install -r requirements.txt --break-system-packages

# Make sure THE_MAIN_ONE.html is in the same directory

# Run locally
python app.py
```

Access at: `http://127.0.0.1:5000`

## 🌐 Deployment (Render)

1. Push this repo to GitHub
2. Go to [render.com](https://render.com)
3. Create new Web Service
4. Connect your GitHub repo
5. Render auto-detects Python and uses:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** Uses Procfile (`gunicorn app:app`)
6. Deploy!

Your app will be live at: `https://your-app-name.onrender.com`

## 📡 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Main FEZZY STATION interface |
| `/api/ip` | Returns IP info (local, external, hostname) |
| `/api/status` | Health check + system info |
| `/health` | Simple OK response for monitoring |

## 🐕 Brand Identity

**Mascot:** Bojack (Labrador × Husky) — Security daemon  
**Codename:** Bojack Fezzy 999  
**Philosophy:** Strategy Over Impulse  
**Creative Modes:** Admin Fezzy vs Intoxicated Fezzy

## 📝 Notes

- No root required — built entirely on rootless Android
- All development done via Termux nano
- Part of the larger FEZZY Security Dashboard ecosystem

---

**Built with:** Flask · Python · Termux · Android  
**Deployed on:** Render  
**© 2026 Grant Fezzy Festers · All Rights Reserved**
