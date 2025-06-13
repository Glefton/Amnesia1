from sqlalchemy.ext.asyncio import AsyncSession
from .models import Player

async def create_player(session: AsyncSession, user_id: int, username: str):
    player = Player(user_id=user_id, username=username)
    session.add(player)
    await session.commit()
    return player

async def get_player(session: AsyncSession, user_id: int):
    return await session.get(Player, user_id)