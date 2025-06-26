from telethon.sync import TelegramClient
from flask import Flask

API_ID = 1234567  # your correct int
API_HASH = 'your_api_hash_here'  # your correct string
BOT_TOKEN = '8176490384:AAHviqKbsu0Xx-HKUOL5_qts1gnCzfl8dvQ'

SESSION_NAME = 'bot'  # or anything, no need to upload .session file

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

app = Flask(__name__)

@app.route("/")
def home():
    return "SmashBot is running!"

if __name__ == "__main__":
    with client:
        client.start(bot_token=BOT_TOKEN)
        app.run(host="0.0.0.0", port=8080)
