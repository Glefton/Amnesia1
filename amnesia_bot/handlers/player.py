from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from keyboards.city_keyboards import get_city_keyboard
from states.game_states import GameStates
from handlers.races import RACE_INFO
from handlers.classes import CLASS_INFO  # Добавьте этот импорт

router = Router()

@router.message(GameStates.choosing_name)
async def process_name(message: Message, state: FSMContext):
    name = message.text.strip()
    if 3 <= len(name) <= 16:
        data = await state.get_data()
        race_info = RACE_INFO[data['race']]
        
        await state.update_data(name=name)
        await state.set_state(GameStates.in_city)
        
        await message.answer(
            f"{race_info['intro']}\n\n"
            f"Ты - {name}, {race_info['name']} {CLASS_INFO[data['character_class']]['name']}\n"
            "Используй кнопки ниже для взаимодействия:",
            reply_markup=get_city_keyboard()
        )
    else:
        await message.answer("Имя должно быть от 3 до 16 символов. Попробуй еще раз.")