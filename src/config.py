import dataclasses
from configparser import ConfigParser


@dataclasses.dataclass
class BotSettings:

    token: str


@dataclasses.dataclass
class RedisSettings:

    host: str
    port: int
    db: int
    password: str


@dataclasses.dataclass
class StorageSettings:

    type: str


@dataclasses.dataclass
class DatabaseSettings:

    url: str


@dataclasses.dataclass
class ConfigStorage:

    bot: BotSettings
    redis: RedisSettings
    storage: StorageSettings
    database: DatabaseSettings

    @classmethod
    def create_from_file(cls, filename: str) -> "ConfigStorage":
        config_parser = ConfigParser()
        config_parser.read(filename)

        return cls(
            bot=BotSettings(**config_parser["bot"]),
            redis=RedisSettings(**config_parser["redis"]),
            storage=StorageSettings(**config_parser["storage"]),
            database=DatabaseSettings(**config_parser["database"])
        )
