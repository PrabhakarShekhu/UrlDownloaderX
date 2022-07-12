

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Button(object):

      BUTTONS01 = InlineKeyboardMarkup( [ [ InlineKeyboardButton(text="❌", callback_data="X0") ] ] )
