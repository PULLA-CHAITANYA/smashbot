from flask import Flask
from telethon.sync import TelegramClient
import os

app = Flask(__name__)

API_ID = int(os.environ.get('API_ID'))  # Set this in Railway variables
API_HASH = os.environ.get('API_HASH')
BOT_TOKEN = os.environ.get('BOT_TOKEN')

SESSION_NAME = 'bot'  # Just a name, no session file required

client = TelegramClient(SESSION_NAME, API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@app.route('/')
def home():
    return "Bot is alive!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
