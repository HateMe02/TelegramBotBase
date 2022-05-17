from aiogram import Dispatcher


def register(dp: Dispatcher) -> None:
    """
    This approach is used to avoid premature registration of the handler, before registering filters.

    example:
        dp.register_message_handler(some_command, *filters, another)
    """
