from flask import Flask, request
import requests
from datetime import datetime

app = Flask(__name__)

# ⚠️ YAHAN APNA DAALNA HAI
TELEGRAM_TOKEN = "7123456789:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw"  # BotFather wala
CHAT_ID = "123456789"  # Tera Chat ID

@app.route('/vantage', methods=['POST'])
def superman_signal():
    data = request.json
    
    pair = data.get('pair', 'XAUUSD')
    direction = data.get('direction', 'BUY') 
    entry = data.get('entry', '4332')
    tp1 = data.get('tp1', '4340')
    tp2 = data.get('tp2', '4350')
    sl = data.get('sl', '4320')
    lot = data.get('lot', '0.01')
    time_now = datetime.now().strftime("%I:%M %p")
    
    msg = f"🦸 SUPERMAN SIGNAL 🦸\n\nPair: {pair}\nAction: {direction}\nEntry: {entry}\nLot: {lot}\n\n🎯 TP1: {tp1}\n🎯 TP2: {tp2}\n🛑 SL: {sl}\n\n⏰ Time: {time_now}"
    
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "HTML"})
    
    return {"status": "Signal Sent", "pair": pair}

@app.route('/')
def home():
    return "Superman Bot Live ✅"

if __name__ == '__main__':
    app.run()
