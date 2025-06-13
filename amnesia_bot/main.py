import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from config import BOT_TOKEN
from handlers import register_handlers
from middlewares import register_middlewares
from database.models import Base
from database.database import engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def on_startup(bot: Bot):
    await create_tables()
    logger.info("Bot started")
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Начать игру"),
        types.BotCommand(command="explore", description="Исследовать мир"),
    ])

async def main():
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode="HTML")
    )
    dp = Dispatcher(storage=MemoryStorage())

    register_middlewares(dp)
    register_handlers(dp)

    try:
        await dp.start_polling(
            bot,
            on_startup=on_startup,
            allowed_updates=dp.resolve_used_update_types()
        )
    except Exception as e:
        logger.error(f"Polling failed: {e}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())