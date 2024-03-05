from telethon.sync import TelegramClient


api_id = input("Enter your Telegram API ID: ")
api_hash = input("Enter your Telegram API hash: ")

client = TelegramClient('session_name', api_id, api_hash)

async def delete_all_messages():
    await client.connect()
    if not await client.is_user_authorized():
        await client.start(phone_number=input("Enter your phone number: "))
    me = await client.get_me()
    dialogs = await client.get_dialogs()

    for dialog in dialogs:
        try:
            await client.delete_dialog(dialog.id)
            print(f"Deleted all messages in {dialog.title}")
        except Exception as e:
            print(f"Error deleting messages in {dialog.title}: {e}")

    await client.disconnect()


with client:
    client.loop.run_until_complete(delete_all_messages())
