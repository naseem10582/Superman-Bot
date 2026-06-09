from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Railway ke Variables se TOKEN aur CHATID lega
TOKEN = os.environ['TOKEN']
CHAT_ID = os.environ['CHATID']

@app.route('/')
def home():
    return "Superman Bot is LIVE! 🚀"

@app.route('/vantage', methods=['POST'])
def alert():
    data = request.get_data(as_text=True)
    
    # Telegram message format
    msg = f"🚀 *XAUUSD SIGNAL* 🚀\n\n{data}"
    
    # Telegram pe bhej dega
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                  json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})
    
    print("TV Alert Received:", data)
    return "OK", 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
