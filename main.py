from flask import Flask
from threading import Thread
from telethon.sync import TelegramClient, events
import os
import asyncio

app = Flask(__name__)

@app.route('/')
def home():
    return "SmashBot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()

API_ID = int(os.environ['API_ID'])
API_HASH = os.environ['API_HASH']
SESSION_NAME = "smashbot"
seen_links = set()

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

@client.on(events.NewMessage(chats='mainet_community'))
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

client.start()
print("✅ SmashBot is running. Waiting for raids in mainet_community...")
client.run_until_disconnected()
