from aiogram import executor

from handlers.admins.admins import register_admin_py
from handlers.users.users import register_users_py
from loader import dp
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)

    register_admin_py(dispatcher)

    register_users_py(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

