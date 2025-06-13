import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN") or ""
DATABASE_URL = "sqlite+aiosqlite:///database.db"