from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_classes_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="⚔️ Воин", callback_data="class_warrior")
    builder.button(text="🔮 Маг", callback_data="class_mage")
    builder.button(text="🏹 Следопыт", callback_data="class_ranger")
    builder.adjust(1)
    return builder.as_markup()

def get_class_confirmation_keyboard(class_type: str):
    builder = InlineKeyboardBuilder()
    builder.button(text="✅ Подтвердить", callback_data=f"confirm_class_{class_type}")
    builder.button(text="🔙 Назад", callback_data="back_to_classes")
    builder.adjust(2)
    return builder.as_markup()