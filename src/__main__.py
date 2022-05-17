from aiogram.utils import executor

from src import signals
from src.vars import dp

if __name__ == "__main__":
    executor.start_polling(
        dp,
        on_startup=signals.on_startup,
        on_shutdown=signals.on_shutdown
    )
