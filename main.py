from flask import Flask, request
import requests
import threading
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

app = Flask(__name__)

TELEGRAM_TOKEN = "8035652460:AAEphHieXtY-4YE_1z2w0F4_5wKy_h4nK-A"
CHAT_ID = "7752283157"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🦸 SUPERMAN BOT ONLINE ✅\n/gold likh ke signal le")

# /gold command  
async def gold(update: Update, context: ContextTypes.DEFAULT_TYPE):
    signal_msg = """
🦸 SUPERMAN GOLD SIGNAL 🦸
Pair: XAUUSD
Action: BUY
Entry: 4352.00
TP1: 4357.00
TP2: 4362.00
SL: 4347.00
Lot Size: 0.01
Time: NOW
"""
    await update.message.reply_text(signal_msg)

# Flask route for health check
@app.route('/')
def home():
    return "Superman Bot Running"

# Flask route for MT5 signals
@app.route('/signal', methods=['POST'])
def signal():
    data = request.json
    signal_msg = f"""
🦸 SUPERMAN SIGNAL 🦸
Pair: {data.get('pair')}
Action: {data.get('direction')}
Entry: {data.get('entry')}
TP1: {data.get('tp1')}
TP2: {data.get('tp2')}
SL: {data.get('sl')}
Lot Size: {data.get('lot')}
"""
    requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", 
                  json={"chat_id": CHAT_ID, "text": signal_msg})
    return "Signal Sent"

# Bot ko background mein chalao
def run_bot():
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("gold", gold))
    application.run_polling()

if __name__ == '__main__':
    # Bot ko alag thread mein start karo
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()
    # Flask server chalao
    app.run(host='0.0.0.0', port=8080)
