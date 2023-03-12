from aiogram.dispatcher.filters.state import StatesGroup, State


class AdminState(StatesGroup):
    send_message = State()
