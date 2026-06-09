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

⚠️ Valid for
