from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from keyboards.races import get_races_keyboard, get_race_confirmation_keyboard
from keyboards.classes import get_classes_keyboard
from states.game_states import GameStates

router = Router()

RACE_INFO = {
    "human": {
        "name": "👨 Человек",
        "stats": {"int": 2, "str": 2, "agi": 2, "end": 2},
        "desc": (
            "Универсальная раса без слабостей\n\n"
            "🧠 Интеллект: 2\n"
            "💪 Сила: 2\n"
            "🏃 Ловкость: 2\n"
            "🛡️ Выносливость: 2\n\n"
            "Сбалансированные характеристики"
        ),
        "intro": "Вы очнулись на окраине человеческого королевства..."
    },
    "elf": {
        "name": "🧝 Эльф", 
        "stats": {"int": 3, "str": 1, "agi": 3, "end": 1},
        "desc": (
            "Мастера магии и стрельбы\n\n"
            "🧠 Интеллект: 3\n"
            "💪 Сила: 1\n"
            "🏃 Ловкость: 3\n"
            "🛡️ Выносливость: 1\n\n"
            "Идеальны для магических классов"
        ),
        "intro": "Вы приходите в сознание в священной эльфийской роще..."
    },
    "orc": {
        "name": "👹 Орк",
        "stats": {"int": 1, "str": 3, "agi": 1, "end": 3},
        "desc": (
            "Могучие воины\n\n"
            "🧠 Интеллект: 1\n"
            "💪 Сила: 3\n"
            "🏃 Ловкость: 1\n"
            "🛡️ Выносливость: 3\n\n"
            "Неудержимые в ближнем бою"
        ),
        "intro": "Вы открываете глаза в дымящихся землях орков..."
    },
    "lich": {
        "name": "💀 Лич",
        "stats": {"int": 4, "str": 1, "agi": 1, "end": 2},
        "desc": (
            "Повелители магии смерти\n\n"
            "🧠 Интеллект: 4\n"
            "💪 Сила: 1\n"
            "🏃 Ловкость: 1\n"
            "🛡️ Выносливость: 2\n\n"
            "Мощные заклинатели"
        ),
        "intro": "Тьма рассеивается, и вы понимаете, что находитесь в некрополисе..."
    }
}

@router.callback_query(F.data == "back_to_races")
async def back_to_races(callback: CallbackQuery, state: FSMContext):
    await state.set_state(GameStates.choosing_race)
    await callback.message.edit_text(
        "Выбери свою расу:",
        reply_markup=get_races_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data.startswith("race_"), GameStates.choosing_race)
async def select_race(callback: CallbackQuery):
    race = callback.data.split("_")[1]
    info = RACE_INFO[race]
    await callback.message.edit_text(
        info['desc'],
        reply_markup=get_race_confirmation_keyboard(race)
    )
    await callback.answer()

@router.callback_query(F.data.startswith("confirm_race_"), GameStates.choosing_race)
async def confirm_race(callback: CallbackQuery, state: FSMContext):
    race = callback.data.split("_")[2]
    await state.update_data(race=race)
    await state.set_state(GameStates.choosing_class)
    await callback.message.edit_text(
        f"Вы выбрали расу: {RACE_INFO[race]['name']}\n"
        "Теперь выбери класс:",
        reply_markup=get_classes_keyboard()
    )
    await callback.answer()