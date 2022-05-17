from aiogram import Dispatcher


def register(dp: Dispatcher) -> None:
    """
    Registering middleware

    example:
        dp.setup_middleware(MyMiddleware())

    """
