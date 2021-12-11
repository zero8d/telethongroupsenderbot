from telethon import TelegramClient, client, events

# Use your own values from my.telegram.org
api_id = 17640419
api_hash = '34640e1ab0b2eddb24e27b7c46e39326'
from telethon import TelegramClient
chat = -361437575
client = TelegramClient('zero8d', api_id, api_hash)

client.start()

@client.on(events.NewMessage(chats=chat))
async def evh(event):
    async for dialog in client.iter_dialogs():
        if(dialog.is_group and dialog.id!=chat):
            print(dialog.is_group)
            await client.send_message(dialog.input_entity, event.message)
    await client.send_message(chat, "message has been sent")
client.run_until_disconnected()