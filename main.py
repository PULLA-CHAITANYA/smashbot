from flask import Flask
from telethon import TelegramClient, events

API_ID = 25749247
API_HASH = '5c8f9cdbed12339f4d1d9414a0151bc7'
BOT_TOKEN = '8176490384:AAHviqKbsu0Xx-HKUOL5_qts1gnCzfl8dvQ'
SESSION_NAME = 'bot.session'

app = Flask(__name__)

# Reuse session to prevent repeated logins
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

async def start_bot():
    if not await client.is_user_authorized():
        await client.start(bot_token=BOT_TOKEN)

# Event: /start
@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    await event.respond("👋 Hello! Bot is alive.")
    print(f"Started with @{event.sender.username}")

# Event: All other messages
@client.on(events.NewMessage)
async def reply_handler(event):
    if event.text != "/start":
        await event.respond("🤖 Bot received your message.")
        print(f"Echoed: {event.text}")

@app.route('/')
def index():
    return "✅ Bot is running!"

# Launch everything
if __name__ == '__main__':
    import asyncio
    import threading

    def run_telegram():
        asyncio.run(start_bot())
        client.run_until_disconnected()

    threading.Thread(target=run_telegram).start()
    app.run(host='0.0.0.0', port=8080)
