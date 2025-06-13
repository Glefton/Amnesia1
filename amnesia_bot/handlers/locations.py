from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

@router.callback_query(F.data == "explore")
async def explore_location(callback: CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.button(text="🏰 В город", callback_data="city")
    builder.button(text="🌲 В лес", callback_data="forest")
    builder.button(text="⚔️ На охоту", callback_data="hunt")
    
    await callback.message.answer(
        "Куда вы хотите отправиться?",
        reply_markup=builder.as_markup()
    )