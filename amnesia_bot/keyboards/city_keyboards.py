def get_npcs_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="1. Торговец", callback_data="npc_merchant")
    builder.button(text="2. Кузнец", callback_data="npc_blacksmith")
    builder.button(text="3. Задания", callback_data="npc_quest")
    builder.button(text="⬅️ Назад", callback_data="back_to_city")
    builder.adjust(1)
    return builder.as_markup()

def get_npc_interaction_keyboard(npc_type: str):
    builder = InlineKeyboardBuilder()
    
    if npc_type == "merchant":
        builder.button(text="🛒 Торговля", callback_data="open_shop")
    elif npc_type == "blacksmith":
        builder.button(text="⚒️ Ремонт", callback_data="repair_gear")
        builder.button(text="⚔️ Улучшить", callback_data="upgrade_gear")
    elif npc_type == "quest":
        builder.button(text="📜 Взять квест", callback_data="take_quest")
        builder.button(text="✅ Сдать квест", callback_data="complete_quest")
    
    builder.button(text="💬 Поговорить", callback_data=f"talk_{npc_type}")
    builder.button(text="⬅️ Назад", callback_data="city_npcs")
    builder.adjust(2)
    return builder.as_markup()