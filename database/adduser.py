from pyrogram import Client
from database.access import botly
from pyrogram.types import Message


async def AddUser(bot: Client, update: Message):
    if not await botly.is_user_exist(update.from_user.id):
           await botly.add_user(update.from_user.id)
