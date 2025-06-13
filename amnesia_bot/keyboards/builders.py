from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_races_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="🧝 Эльф", callback_data="race_elf")
    builder.button(text="👨 Человек", callback_data="race_human")
    builder.button(text="👹 Орк", callback_data="race_orc")
    builder.button(text="💀 Лич", callback_data="race_lich")
    builder.adjust(2)
    return builder.as_markup()

def get_race_confirmation_keyboard(race: str):
    builder = InlineKeyboardBuilder()
    builder.button(text="✅ Подтвердить", callback_data=f"confirm_race_{race}")
    builder.button(text="❌ Назад", callback_data="back_to_races")
    builder.adjust(2)
    return builder.as_markup()

def get_classes_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="🛡️ Воин", callback_data="class_warrior")
    builder.button(text="🔮 Маг", callback_data="class_mage")
    builder.button(text="🏹 Следопыт", callback_data="class_ranger")
    builder.adjust(2)
    return builder.as_markup()
    
def get_nickname_cancel_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="❌ Отменить", callback_data="cancel_nickname")
    return builder.as_markup()

def get_battle_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="⚔️ Атаковать", callback_data="battle_attack")
    builder.button(text="🛡️ Защищаться", callback_data="battle_defend")
    builder.button(text="🏃‍♂️ Бежать", callback_data="battle_flee")
    builder.button(text="🧪 Использовать зелье", callback_data="battle_potion")
    builder.adjust(2)
    return builder.as_markup()