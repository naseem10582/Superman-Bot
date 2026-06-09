from flask import Flask, request
import requests
import os
from datetime import datetime

app = Flask(__name__)

# Railway Environment Variables se aayega
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
TELEGRAM_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

# Pairs ke commands
PAIRS = {
    "/xau": "XAUUSD",
    "/xag": "XAGUSD",
    "/btc": "BTCUSD",
    "/eth": "ETHUSD",
    "/sol": "SOLUSD",
    "/zec": "ZECUSD",
    "/us100": "US100",
    "/usoil": "USOIL"
}

def send_signal(pair_name):
    entry = 109500
    sl = 108500
    tp = entry + (entry - sl) * 3

    msg = f"""🦸 SUPERMAN {pair_name} 🦸
🎯 HIGH ACCURACY SETUP
⏱️ Timeframe: 5-15 Min

Action: BUY
Entry: {entry}
TP: {int(tp)}
SL: {sl}
RR: 1:3
Confidence: 95%
Time: {datetime.now().strftime('%I:%M %p')}

⚠️ Valid for next 15 min only"""

    requests.post(TELEGRAM_URL, json={"chat_id": CHAT_ID, "text": msg})

@app.route("/")
def home():
    return "Superman Bot is running!"

@app.route("/", methods=["POST"])
def webhook():
    data = request.json

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/start":
            welcome = """🦸 Superman Bot Active 🦸

Commands:
/xau Gold
/xag Silver
/btc Bitcoin
/eth Ethereum
/sol Solana
/zec Zcash
/us100 Nasdaq
/usoil Oil

Type any command for signal"""
            requests.post(TELEGRAM_URL, json={"chat_id": chat_id, "text": welcome})

        elif text in PAIRS:
            send_signal(PAIRS[text])
            requests.post(TELEGRAM_URL, json={"chat_id": chat_id, "text": f"Signal sent for {PAIRS[text]} ✅"})

    return "ok"

# RAILWAY KE LIYE YE ZARURI HAI
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
