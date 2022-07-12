from pyrogram import Client as Botly
from pyrogram import filters
from config import Config
from database.access import botly
from plugins.buttons import *
@Botly.on_message(filters.private & filters.command('total'))
async def sts(c, m):
    if m.from_user.id != Config.OWNER_ID:
        return 
    total_users = await botly.total_users_count()
    await m.reply_text(text=f"Total user(s) {total_users}", quote=True)


@Botly.on_message(filters.private & filters.command("search"))
async def serc(bot, update):

      await bot.send_message(chat_id=update.chat.id, text="🔍 TORRENT SEARCH", 
      parse_mode="html", reply_markup=Button.BUTTONS01)
