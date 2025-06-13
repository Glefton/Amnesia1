from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.dispatcher import Dispatcher
from typing import Callable, Dict, Any, Awaitable
import logging

logger = logging.getLogger(__name__)

class LoggingMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        logger.info(f"Processing {event.__class__.__name__}")
        return await handler(event, data)

def register_middlewares(dp: Dispatcher):
    dp.update.outer_middleware(LoggingMiddleware())