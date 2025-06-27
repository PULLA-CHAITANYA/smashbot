from telethon import TelegramClient, events
from flask import Flask
import asyncio

# === Replace these with your actual credentials ===
API_ID = 25749247
  # 🟡 Your actual API_ID (no quotes)
API_HASH = "5c8f9cdbed12339f4d1d9414a0151bc7"  # 🟡 Your actual API_HASH (quotes okay)
BOT_TOKEN = "8176490384:AAHviqKbsu0Xx-HKUOL5_qts1gnCzfl8dvQ"  # 🟡 Your bot token from BotFather

# === Dummy session name for bot; session file will not be created ===
client = TelegramClient("bot", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 Bot is live!"

@client.on(events.NewMessage)
async def handler(event):
    await event.reply("✅ Bot received your message!")

# === Run Flask + Telethon together ===
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(client.run_until_disconnected())
    app.run(host="0.0.0.0", port=8080)
