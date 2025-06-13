from aiogram import Dispatcher
from .start import router as start_router
from .races import router as races_router
from .classes import router as classes_router
from .nickname import router as nickname_router
from .locations import router as locations_router
from .inventory import router as inventory_router
from .npc import router as npc_router
from .exploration import router as exploration_router
from .battle import router as battle_router
from .player import router as player_router
from .quests import router as quests_route

def register_handlers(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(races_router)
    dp.include_router(classes_router)
    dp.include_router(nickname_router)
    dp.include_router(locations_router)
    dp.include_router(inventory_router)
    dp.include_router(npc_router)
    dp.include_router(exploration_router)
    dp.include_router(battle_router)
    dp.include_router(player_router)
    dp.include_router(quests_router
   