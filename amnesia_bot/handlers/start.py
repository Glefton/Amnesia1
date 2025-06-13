from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext  # Добавлен этот импорт
from keyboards.start import get_start_keyboard
from keyboards.races import get_races_keyboard
from states.game_states import GameStates

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "🧿 Добро пожаловать в Amnesia!\n\n"
        "Ты очнулся в темной пещере без воспоминаний...",
        reply_markup=get_start_keyboard()
    )

@router.callback_query(F.data == "start_game")
async def start_game(callback: CallbackQuery, state: FSMContext):
    await state.set_state(GameStates.choosing_race)
    await callback.message.answer(
        "Выбери свою расу:",
        reply_markup=get_races_keyboard()
    )
    await callback.answer()