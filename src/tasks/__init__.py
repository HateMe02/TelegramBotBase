from apscheduler.schedulers.asyncio import AsyncIOScheduler


def register(scheduler: AsyncIOScheduler) -> None:
    """
    Registration of tasks in the scheduler, to avoid various kinds of errors.
    Please note that if your task will be repeated very often—this can slow down the bot,
    in this case you need to run the scheduler in a separate thread (that is, run separately from the bot)

    example:
        scheduler.add_jon(my_job, "interval", seconds=30)

    """
