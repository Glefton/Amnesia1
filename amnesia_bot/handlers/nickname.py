from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.game_states import GameStates

router = Router()

@router.message(GameStates.choosing_nickname)
async def process_nickname(message: Message, state: FSMContext):
    nickname = message.text.strip()
    
    if len(nickname) < 3 or len(nickname) > 20:
        await message.answer("Никнейм должен быть от 3 до 20 символов. Попробуй еще раз:")
        return
    
    await state.update_data(nickname=nickname)
    data = await state.get_data()
    
    race_name = {
        "elf": "🧝 Эльф",
        "human": "👨 Человек",
        "orc": "👹 Орк",
        "lich": "💀 Лич"
    }.get(data['race'], data['race'])
    
    class_name = {
        "warrior": "🛡️ Воин",
        "mage": "🔮 Маг",
        "ranger": "🏹 Следопыт"
    }.get(data['character_class'], data['character_class'])
    
    await message.answer(
        f"🎉 Персонаж создан!\n\n"
        f"Ты - {nickname}\n"
        f"Раса: {race_name}\n"
        f"Класс: {class_name}\n\n"
        "Используй /explore чтобы начать игру!"
    )
    await state.set_state(GameStates.exploring)