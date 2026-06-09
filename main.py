from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = "7997402769:AAGX6DEOKI5v0DNAyOpVYWkTk6Yzrd4Ozsw"
CHAT_ID = "5458457612"

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, json=payload)
        print(response.json())
        return response.json()
    except Exception as e:
        print(f"Error: {e}")
        return None

@app.route('/')
def home():
    send_telegram_message("🦸 <b>SUPERMAN BOT ONLINE</b> ✅\nServer chal raha hai")
    return "Superman Bot Live ✅ Message Bhej Diya - Telegram Check Kar"

@app.route('/signal', methods=['POST'])
def webhook_signal():
    try:
        data = request.get_json()
        
        pair = data.get('pair', 'XAUUSD')
        direction = data.get('direction', 'BUY')
        entry = data.get('entry', 'N/A')
        tp1 = data.get('tp1', 'N/A')
        tp2 = data.get('tp2', 'N/A')
        sl = data.get('sl', 'N/A')
        lot = data.get('lot', '0.01')
        
        message = f"""
🦸 <b>SUPERMAN SIGNAL</b> 🦸

<b>Pair:</b> {pair}
<b>Action:</b> {direction}
<b>Entry:</b> {entry}
<b>Lot Size:</b> {lot}

<b>TP1:</b> {tp1}
<b>TP2:</b> {tp2}
<b>SL:</b> {sl}

<i>Time: 08:00 PM</i>
        """
        
        send_telegram_message(message)
        return {"status": "success"}, 200
        
    except Exception as e:
        return {"status": "error", "message": str(e)}, 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
