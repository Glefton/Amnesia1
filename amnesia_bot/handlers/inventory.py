from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "/inventory")
async def show_inventory(message: Message):
    await message.answer(
        "🎒 Ваш инвентарь:\n"
        "- Зелье здоровья x3\n"
        "- Простая броня\n"
        "- 50 золотых"
    )