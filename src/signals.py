from tortoise import Tortoise

from src import commands, filters, middlewares, tasks
from src.vars import TORTOISE_ORM, dp, scheduler


async def on_startup(_) -> None:
    await Tortoise.init(
        config=TORTOISE_ORM
    )
    await Tortoise.generate_schemas()

    commands.register(dp)
    filters.register(dp)
    middlewares.register(dp)
    tasks.register(scheduler)

    scheduler.start()


async def on_shutdown(_) -> None:
    scheduler.shutdown()
    await Tortoise.close_connections()
