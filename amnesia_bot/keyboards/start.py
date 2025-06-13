from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_start_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="🎮 Начать игру", callback_data="start_game")
    return builder.as_markup()