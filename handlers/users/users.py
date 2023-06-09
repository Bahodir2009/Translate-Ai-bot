from aiogram import Dispatcher
from aiogram.types import *
from database.connections import add_user
from keyboards.inline.users_btns import language_btn
from loader import dp
from utils.misc.text_translate import text_trans


async def bot_start(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    await add_user(user_id, username)
    await message.answer(f"Salom")


async def get_user_text_handler(message: Message):
    text = message.text
    btn = await language_btn()
    await message.answer(text, reply_markup=btn)


async def select_lang_callback(call: CallbackQuery):
    await call.answer()
    lang = call.data.split(":")[-1]
    context = call.message.text
    result = await text_trans(context, lang)
    if context != result:
        btn = await language_btn()
        await call.message.edit_text(result, reply_markup=btn)


def register_users_py(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=['start'])
    dp.register_message_handler(get_user_text_handler, content_types=['text'])

    dp.register_callback_query_handler(select_lang_callback, text_contains='lang:')