from flask import Flask
from threading import Thread
from telethon.sync import TelegramClient, events
import os
import asyncio

# -------------------------------
# Flask server to keep Railway app alive
# -------------------------------
app = Flask(__name__)

@app.route('/')
def home():
    return "SmashBot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()

# -------------------------------
# Telegram Bot Setup
# -------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
SESSION_NAME = "smashbot"

# Create TelegramClient without api_id/api_hash (not used with bot token)
client = TelegramClient(SESSION_NAME, api_id=12345, api_hash='fakehash')  # dummy values for compatibility

# Track links to prevent duplicate "smash"
seen_links = set()

@client.on(events.NewMessage(chats='mainet_community'))  # replace with your group username
async def handler(event):
    message = event.message
    text = message.message

    if message.buttons:
        if "https://" in text:
            start = text.find("https://")
            end = text.find(" ", start)
            tweet_url = text[start:] if end == -1 else text[start:end]
        else:
            tweet_url = None

        if tweet_url and tweet_url in seen_links:
            print(f"[i] Already smashed: {tweet_url}")
            return
        elif tweet_url:
            seen_links.add(tweet_url)

        await asyncio.sleep(10)
        try:
            await message.click(text="Smash")
            print(f"[✓] SMASHED: {tweet_url or 'No link'}")
        except Exception as e:
            print(f"[x] Error smashing: {e}")
    else:
        print("[i] New message received – no buttons found.")

# Start the client with bot token
client.start(bot_token=BOT_TOKEN)
print("✅ SmashBot is running. Waiting for raids in mainet_community...")
client.run_until_disconnected()
