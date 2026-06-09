from flask import Flask, request
import requests
import os

app = Flask(__name__)

# ===== TERA TOKEN + CHAT ID =====
TELEGRAM_TOKEN = "8035652460:AAEphHieXtY-4YE_1z2w0F4_5wKy_h4nK-A"
CHAT_ID = "5458457612"

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    try:
        requests.post(url, json=payload)
    except:
        pass

@app.route('/')
def home():
    send_to_telegram("🦸 <b>SUPERMAN BOT ONLINE</b> ✅\n\nTest successful. Ready for signals.")
    return "Superman Bot Live ✅ Message Bhej Diya - Telegram Check Kar"

@app.route('/signal', methods=['GET', 'POST'])
def signal():
    if request.method == 'POST':
        data = request.get_json() or {}
    else:
        data = request.args
    
    pair = data.get('pair', 'XAUUSD')
    direction = data.get('direction', 'BUY')
    entry = data.get('entry', '4345.00')
    tp1 = data.get
