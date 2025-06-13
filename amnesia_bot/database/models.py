from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase

class Base(AsyncAttrs, DeclarativeBase):
    pass

class Player(Base):
    __tablename__ = "players"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True)
    username = Column(String)
    race = Column(String)
    character_class = Column(String)
    level = Column(Integer, default=1)
    stats = Column(JSON, default={"strength": 5, "agility": 5, "intelligence": 5})
    inventory = Column(JSON, default=[])
    current_location = Column(String, default="start_cave")