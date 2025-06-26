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
    return "✅ SmashBot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()

# -------------------------------
# Telegram Bot Setup
# -------------------------------
API_ID = 12345678  # 🔁 Replace with your actual API ID
API_HASH = "your_api_hash_here"  # 🔁 Replace with your actual API Hash
SESSION_NAME = "smashbot"  # ✅ Should match your .session filename (e.g., smashbot.session)

seen_links = set()

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

# ✅ Use session file instead of asking for phone number
client.connect()
if not client.is_user_authorized():
    print("❌ Session not authorized. Please generate the .session file locally and upload it.")
    exit(1)

@client.on(events.NewMessage(chats='mainet_community'))
async def handler(event):
    message = event.message
    text = message.message

    if message.buttons:
        # Try to extract Twitter link
        tweet_url = None
        if "https://" in text:
            start = text.find("https://")
            end = text.find(" ", start)
            tweet_url = text[start:] if end == -1 else text[start:end]

        # Prevent duplicate smash for same tweet
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

print("✅ SmashBot is running. Waiting for raids in mainet_community...")
client.run_until_disconnected()
