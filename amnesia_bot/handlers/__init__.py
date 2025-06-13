from aiogram import Dispatcher
from .start import router as start_router
from .races import router as races_router
from .classes import router as classes_router
from .player import router as player_router
from .city import router as city_router
from .quests import router as quests_router

def register_handlers(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(races_router)
    dp.include_router(classes_router)
    dp.include_router(player_router)
    dp.include_router(city_router)
    dp.include_router(quests_router)