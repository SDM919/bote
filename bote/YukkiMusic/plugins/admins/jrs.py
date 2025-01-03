from pyrogram import Client, filters
from pyrogram.types import Message
from YukkiMusic import app
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


@app.on_message(
    command(["السورس", "سورس", "المبرمج"])
)
async def mak(client: Client, message: Message):
    await message.reply_photo(
        photo="https://t.me/imgtelebok/17",
        caption="~ Team 𝐀𝐑𝐀𝐁𝐒 \n~ Dav Source",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⦗ Dev ⦘", url="https://t.me/V1SDM"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "⦗ Updates ⦘", url="https://t.me/V1PHP"
                    ),
                    InlineKeyboardButton(
                        "⦗ support ⦘", url="https://t.me/V1SDM"
                    ),
                ],
            ]
        ),
    )
