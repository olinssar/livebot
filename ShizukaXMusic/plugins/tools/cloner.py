from telethon import TelegramClient, events
from config import API_ID, API_HASH
import sys
import telethon

@Zaid.on(events.NewMessage(pattern="^[?!/]clone"))
async def clone(msg):
    chat = msg.chat_id
    text = await msg.reply("Usage:\n\n /clone token")
    phone = msg.text.split(maxsplit=1)[1]
    try:
        await text.edit("Booting Your Client")
        cli = TelegramClient(":memory:", api_id=API_ID, api_hash=API_HASH)
        await cli.start(bot_token=phone)
        for cmd in HANDLER:
            cli.add_event_handler(cmd)
        user = await cli.get_me()
        userid = telethon.utils.get_peer_id(user)
        await msg.reply(f"Your Client Has Been Successfully Started As {userid}! ✅\n\nThanks for Cloning.\nDon't Forget to Join Our @Alinallmovies")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
#End￼Enter
