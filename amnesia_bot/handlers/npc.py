from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder
from database.crud import get_player

router = Router()

NPC_DATA = {
    "illirien": {
        "npc1": {
            "name": "Эльфийский наставник Лириан",
            "description": "Древний эльф с глазами, полными мудрости веков.",
            "dialog": "Приветствую, дитя леса...",
            "options": {
                "Узнать о лесе": "Лес Селарион хранит множество тайн...",
                "Получить задание": "Найди 5 светящихся грибов...",
                "Уйти": "Да пребудет с тобой свет звёзд."
            }
        }
    }
}

def get_npc_keyboard(npc_options):
    builder = InlineKeyboardBuilder()
    for option in npc_options.keys():
        builder.button(text=option, callback_data=f"npc_option_{option}")
    builder.adjust(1)
    return builder.as_markup()

@router.callback_query(F.data.startswith("talk_npc"))
async def interact_npc(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    race = data.get('race', 'human')
    npc_id = "npc1"  # Упрощенная логика для примера
    
    npc = NPC_DATA[race.lower()][npc_id]
    
    await callback.message.answer(
        f"*{npc['name']}*\n\n"
        f"{npc['description']}\n\n"
        f"*Говорит:* {npc['dialog']}",
        parse_mode="Markdown",
        reply_markup=get_npc_keyboard(npc["options"])
    )

@router.callback_query(F.data.startswith("npc_option_"))
async def handle_npc_option(callback: CallbackQuery, state: FSMContext):
    option = callback.data.split("_")[2]
    data = await state.get_data()
    race = data.get('race', 'human')
    npc = NPC_DATA[race.lower()]["npc1"]
    
    await callback.message.answer(
        f"*{npc['name']}*\n\n"
        f"{npc['options'][option]}",
        parse_mode="Markdown"
    )