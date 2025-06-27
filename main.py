from flask import Flask
from telethon import TelegramClient, events

# Your Telegram credentials
API_ID = 25749247
API_HASH = '5c8f9cdbed12339f4d1d9414a0151bc7'
BOT_TOKEN = '8176490384:AAHviqKbsu0Xx-HKUOL5_qts1gnCzfl8dvQ'

SESSION_NAME = 'bot_session'

# Initialize Flask app
app = Flask(__name__)

# Initialize Telegram client with bot token
client = TelegramClient(SESSION_NAME, API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# Telegram message handler
@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    await event.respond("👋 Hello! Bot received your /start command.")
    print(f"[LOG] Replied to /start from @{event.sender.username}")

@client.on(events.NewMessage)
async def echo_handler(event):
    if event.text != "/start":
        await event.respond("🤖 Bot received your message!")
        print(f"[LOG] Echoed to @{event.sender.username}: {event.text}")

# Flask root route
@app.route('/')
def index():
    return "✅ Bot is running!"

# Run both Flask and Telegram bot
if __name__ == '__main__':
    import threading
    threading.Thread(target=client.run_until_disconnected).start()
    app.run(host='0.0.0.0', port=8080)
