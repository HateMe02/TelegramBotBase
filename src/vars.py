from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from src.config import ConfigStorage

config_storage = ConfigStorage.create_from_file("config.ini")

bot = Bot(config_storage.bot.token)
storage = RedisStorage2(
    host=config_storage.redis.host,
    port=config_storage.redis.port,
    db=config_storage.redis.db,
    password=config_storage.redis.password
) if config_storage.storage.type == "redis" else MemoryStorage()
dp = Dispatcher(bot, storage=storage)
scheduler = AsyncIOScheduler()


TORTOISE_ORM = {
    "connections": {"default": config_storage.database.url},
    "apps": {
        "models": {
            "models": ["src.models", "aerich.models"],
            "default_connection": "default",
        },
    }
}
