from telethon import TelegramClient, events

# Remember to use your own values from my.telegram.org!
api_id = 20134319
api_hash = '45e0e7af92588aaa690745741881151d'
client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'hello' in event.raw_text:
        await event.reply('hi!')

client.start()
client.run_until_disconnected()

