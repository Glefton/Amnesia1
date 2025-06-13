from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

router = Router()

@router.callback_query(F.data == "show_quests")
async def show_quests(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    kills = data.get('kills', 0)
    
    if kills >= 5:
        weapons = {
            "warrior": "⚔️ Стальной меч",
            "mage": "🔮 Магический посох",
            "ranger": "🏹 Крепкий лук"
        }
        weapon = weapons.get(data.get('character_class', 'warrior'), "⚔️ Оружие")
        
        await callback.message.answer(
            f"✅ Квест выполнен!\n"
            f"Награда: {weapon}"
        )
        await state.update_data(weapon=weapon)
    else:
        await callback.message.answer(
            f"⚔️ Убейте 5 мобов ({kills}/5)\n"
            "Награда: улучшенное оружие"
        )
    await callback.answer()