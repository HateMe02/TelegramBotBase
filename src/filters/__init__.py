from aiogram import Dispatcher


def register(dp: Dispatcher) -> None:
    """
    Registration of filters, for future access by keys in handlers, that is
        @dp.message_handler(own_filter=value)

    example:
        dp.bind_filter(OwnFilter)
    """
