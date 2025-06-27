from telethon.sync import TelegramClient, events
from flask import Flask

app = Flask(__name__)

API_ID = 123456  # Replace with your actual API_ID
API_HASH = 'your_api_hash'  # Replace with your actual API_HASH
BOT_TOKEN = 'your_bot_token'  # Replace with your actual bot token
SESSION_NAME = 'bot'

client = TelegramClient(SESSION_NAME, API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@app.route('/')
def home():
    return 'Bot is running!'

# Listen for new messages
@client.on(events.NewMessage)
async def handler(event):
    print(f"New message: {event.message.text}")
    await event.reply("Hello from Railway! 🤖")

# Start both Flask and Telegram client
if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.create_task(client.run_until_disconnected())
    app.run(host='0.0.0.0', port=8080)
