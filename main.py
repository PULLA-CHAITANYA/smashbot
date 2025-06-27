from telethon import TelegramClient, events
from flask import Flask
import asyncio

# === Replace these with your actual credentials ===
API_ID = 25749247

API_HASH = "5c8f9cdbed12339f4d1d9414a0151bc7"
BOT_TOKEN = "8176490384:AAHviqKbsu0Xx-HKUOL5_qts1gnCzfl8dvQ"

# === Dummy session name for bot; no session file needed ===
client = TelegramClient("bot", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 Bot is running!"

@client.on(events.NewMessage)
async def handler(event):
    if event.out:
        return  # Don't respond to your own bot's messages
    await event.reply("✅ Bot received your message!")

# === Run Flask and Telegram client together ===
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(client.run_until_disconnected())
    app.run(host="0.0.0.0", port=8080)
