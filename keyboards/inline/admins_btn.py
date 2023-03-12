from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def admin_btn():
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        InlineKeyboardButton("📩 Xabar Yo`llash", callback_data='send')
    )
    return btn
