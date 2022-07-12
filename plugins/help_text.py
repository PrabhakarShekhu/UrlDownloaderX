#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

from config import Config
# the Strings used for this "thing"
from translation import Translation 

from pyrogram import filters
from database.adduser import AddUser
from pyrogram import Client as Botly
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Botly.on_message(filters.private & filters.command(["help"]))
async def help_user(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@Botly.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(update.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Source code", url="https://telegram.me/ZX_bots"
                    ),
                    InlineKeyboardButton("Project Channel", url="https://telegram.me/ZX_bots"),
                ],
                [InlineKeyboardButton("Share", url="https://telegram.me/share/url?url=https://telegram.me/ZX_bots")],
            ]
        ),
        reply_to_message_id=update.message_id
    )
