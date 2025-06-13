from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from keyboards.exploration import get_exploration_keyboard
from keyboards.city_keyboards import get_city_keyboard
from states.game_states import GameStates

router = Router()

@router.message(Command("explore"))
async def explore_command(message: Message, state: FSMContext):
    await message.answer(
        "Вы исследуете окрестности:",
        reply_markup=get_exploration_keyboard()
    )
    await state.set_state(GameStates.exploring)

@router.callback_query(F.data == "enter_city")
async def enter_city(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    race = data.get('race', 'human')
    
    city_descriptions = {
        "human": "🏰 Вы входите в шумный человеческий город Астерию...",
        "elf": "🌳 Вы попадаете в утопающий в зелени эльфийский Иллириан...",
        "orc": "🔥 Вы входите в дымящийся оркский лагерь Грак'Тор...",
        "lich": "💀 Вы проходите через ворота Некрополиса..."
    }
    
    await callback.message.answer(
        city_descriptions[race],
        reply_markup=get_city_keyboard()
    )
    await state.set_state(GameStates.in_city)
    await callback.answer()