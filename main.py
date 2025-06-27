from telethon import TelegramClient, events
from flask import Flask
import asyncio
import os

# === Set your real credentials here ===
API_ID = 25749247
  # Replace with your actual API ID
API_HASH = "5c8f9cdbed12339f4d1d9414a0151bc7"  # Replace with your actual API hash
BOT_TOKEN = "8176490384:AAHviqKbsu0Xx-HKUOL5_qts1gnCzfl8dvQ"  # Replace with your bot token

SESSION_NAME = "bot"  # Just a dummy name; won't store .session

# === Create client ===
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

# === Flask app ===
app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 Bot is running!"

# === Register events only once ===
@client.on(events.NewMessage)
async def handler(event):
    if event.out or event.is_private is False:
        return  # Ignore bot's own messages and group messages
    await event.reply("✅ Bot received your message!")

async def start_bot():
    await client.start(bot_token=BOT_TOKEN)
    print("🤖 Bot is running...")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(start_bot())
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
