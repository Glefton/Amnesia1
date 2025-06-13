from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_exploration_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="🏰 В город", callback_data="enter_city")
    builder.button(text="🌲 Исследовать лес", callback_data="explore_forest")
    builder.button(text="🏔️ Отправиться в горы", callback_data="explore_mountains")
    builder.adjust(1)
    return builder.as_markup()