from flask import Flask
from telethon import TelegramClient, events
import asyncio
import threading

# === Telegram credentials ===
API_ID = 25749247
API_HASH = "5c8f9cdbed12339f4d1d9414a0151bc7"
BOT_TOKEN = "8176490384:AAHviqKbsu0Xx-HKUOL5_qts1gnCzfl8dvQ"
SESSION_NAME = "bot"  # This is arbitrary, won't create a file

app = Flask(__name__)
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

async def start_bot():
    await client.start(bot_token=BOT_TOKEN)
    
    @client.on(events.NewMessage)
    async def handler(event):
        await event.respond("Bot received your message!")
        print(f"Received message: {event.text}")

    print("Bot is running...")
    await client.run_until_disconnected()

def run_telegram():
    asyncio.run(start_bot())

@app.route("/")
def home():
    return "Bot is running!"

if __name__ == "__main__":
    threading.Thread(target=run_telegram).start()
    app.run(host="0.0.0.0", port=8080)
