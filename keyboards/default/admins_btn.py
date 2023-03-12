from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

remove = ReplyKeyboardRemove()


async def cancel_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row('❌ Bekor qilish')
    return btn
