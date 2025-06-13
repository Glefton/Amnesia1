from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

MOBS = {
    "elf": {
        "name": "Лесная тварь",
        "hp": 30,
        "damage": "5-10",
        "exp": 15
    },
    "human": {
        "name": "Бандит",
        "hp": 25,
        "damage": "7-12",
        "exp": 12
    },
    "orc": {
        "name": "Снежный волк",
        "hp": 35,
        "damage": "8-15",
        "exp": 18
    },
    "lich": {
        "name": "Потерянная душа",
        "hp": 20,
        "damage": "10-20",
        "exp": 20
    }
}

@router.callback_query(F.data == "city_map")
async def city_map(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    race = data.get('race', 'human')
    mob = MOBS[race]
    
    builder = InlineKeyboardBuilder()
    builder.button(text="⚔️ Атаковать", callback_data="start_combat")
    builder.button(text="🏰 Вернуться в город", callback_data="enter_city")
    
    await callback.message.answer(
        f"🗺️ Ты прибыл в {QUESTS[race]['location']}\n\n"
        f"Перед тобой {mob['name']} (HP: {mob['hp']})\n"
        f"Опасность: {mob['damage']} урона за удар",
        reply_markup=builder.as_markup()
    )