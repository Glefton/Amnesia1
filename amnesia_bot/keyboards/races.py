from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_races_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="👨 Человек", callback_data="race_human")
    builder.button(text="🧝 Эльф", callback_data="race_elf")
    builder.button(text="👹 Орк", callback_data="race_orc")
    builder.button(text="💀 Лич", callback_data="race_lich")
    builder.adjust(2)
    return builder.as_markup()

def get_race_confirmation_keyboard(race: str):
    builder = InlineKeyboardBuilder()
    builder.button(text="✅ Подтвердить", callback_data=f"confirm_race_{race}")
    builder.button(text="🔙 Назад", callback_data="back_to_races")
    builder.adjust(2)
    return builder.as_markup()