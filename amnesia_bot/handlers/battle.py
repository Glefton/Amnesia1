from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from states.game_states import GameStates

router = Router()

@router.callback_query(F.data == "start_battle")
async def start_battle(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        "⚔️ Вы вступили в бой!\n\n"
        "Выберите действие:",
        reply_markup=get_battle_keyboard()
    )
    await state.set_state(GameStates.in_battle)

def get_battle_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="⚔️ Атаковать", callback_data="battle_attack")
    builder.button(text="🛡️ Защищаться", callback_data="battle_defend")
    builder.button(text="🏃‍♂️ Бежать", callback_data="battle_flee")
    builder.adjust(1)
    return builder.as_markup()