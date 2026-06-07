from flask import Flask, request
import requests
import os

app = Flask(__name__)
TOKEN = os.environ['TOKEN']
CHAT_ID = os.environ['CHATID']

@app.route('/vantage', methods=['POST'])
def alert():
    data = request.get_data(as_text=True)
    msg = f"🦸‍♂️ *XAUUSD SIGNAL* 🦸‍♂️\n\n{data}\n\n*Lot:* 0.01 | *SL:* $0.60\n*Rule:* 7-10 PM IST Only"
    
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                  json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
