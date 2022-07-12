from pyrogram import Botly
from database.access import botly
from pyrogram.types import Message


async def AddUser(bot: Botly, update: Message):
    if not await botly.is_user_exist(update.from_user.id):
           await botly.add_user(update.from_user.id)