from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from keyboards.classes import get_classes_keyboard, get_class_confirmation_keyboard
from keyboards.races import get_races_keyboard
from states.game_states import GameStates

router = Router()

CLASS_INFO = {
    "warrior": {
        "name": "⚔️ Воин",
        "stats": {"str": 3, "int": 1, "agi": 2, "end": 3},
        "desc": (
            "Мастер ближнего боя\n\n"
            "💪 Сила: +3\n"
            "🧠 Интеллект: +1\n"
            "🏃 Ловкость: +2\n"
            "🛡️ Выносливость: +3\n\n"
            "Стартовое оружие: Ржавый меч"
        ),
        "weapon": "⚔️ Ржавый меч"
    },
    "mage": {
        "name": "🔮 Маг",
        "stats": {"int": 3, "str": 1, "agi": 1, "end": 2},
        "desc": (
            "Повелитель магии\n\n"
            "🧠 Интеллект: +3\n"
            "💪 Сила: +1\n"
            "🏃 Ловкость: +1\n"
            "🛡️ Выносливость: +2\n\n"
            "Стартовое оружие: Простой посох"
        ),
        "weapon": "🔮 Простой посох"
    },
    "ranger": {
        "name": "🏹 Следопыт",
        "stats": {"agi": 3, "str": 2, "int": 1, "end": 2},
        "desc": (
            "Меткий стрелок\n\n"
            "🏃 Ловкость: +3\n"
            "💪 Сила: +2\n"
            "🧠 Интеллект: +1\n"
            "🛡️ Выносливость: +2\n\n"
            "Стартовое оружие: Деревянный лук"
        ),
        "weapon": "🏹 Деревянный лук"
    }
}

@router.callback_query(F.data == "back_to_classes")
async def back_to_classes(callback: CallbackQuery, state: FSMContext):
    await state.set_state(GameStates.choosing_class)
    await callback.message.edit_text(
        "Выбери свой класс:",
        reply_markup=get_classes_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data.startswith("class_"), GameStates.choosing_class)
async def select_class(callback: CallbackQuery):
    class_type = callback.data.split("_")[1]
    info = CLASS_INFO[class_type]
    await callback.message.edit_text(
        info['desc'],
        reply_markup=get_class_confirmation_keyboard(class_type)
    )
    await callback.answer()

@router.callback_query(F.data.startswith("confirm_class_"), GameStates.choosing_class)
async def confirm_class(callback: CallbackQuery, state: FSMContext):
    class_type = callback.data.split("_")[2]
    await state.update_data(
        character_class=class_type,
        weapon=CLASS_INFO[class_type]["weapon"],
        kills=0
    )
    await state.set_state(GameStates.choosing_name)
    await callback.message.edit_text(
        "Отлично! Теперь введи имя своего персонажа (от 3 до 16 символов):"
    )
    await callback.answer()