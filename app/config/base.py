from pathlib import Path
from pydantic import ConfigDict, PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parents[2]
ENV_FILE_PATH = BASE_DIR / ".env"


class AppSettings(BaseSettings):
    model_config = ConfigDict(env_prefix="APP_", env_file=ENV_FILE_PATH)

    title: str = "app name"
    host: str = "localhost"
    port: int = 8000
    debug: bool = True
    reload: bool = True


class Redis(BaseSettings):
    model_config = ConfigDict(env_prefix="REDIS_", env_file=ENV_FILE_PATH)
    dsn: RedisDsn = "redis://localhost:6379"


class PostgreSQL(BaseSettings):
    __separator = "://"
    model_config = ConfigDict(env_prefix="POSTGRESQL_", env_file=ENV_FILE_PATH)

    dsn: PostgresDsn

    def build_using_new_scheme(self, scheme: str) -> str:
        return f"{self.__separator}".join(
            [scheme, str(self.dsn).split(sep=self.__separator)[1]],
        )

    @property
    def using_async_driver_for_test(self) -> str:
        split_new_scheme = self.build_using_new_scheme(
            scheme="postgresql+asyncpg"
        ).split("/")
        return "/".join(split_new_scheme[:-1] + [f"test_{split_new_scheme[-1]}"])

    @property
    def using_sync_driver(self) -> str:
        return self.build_using_new_scheme(scheme="postgresql+psycopg2")

    @property
    def using_async_driver(self) -> str:
        return self.build_using_new_scheme(scheme="postgresql+asyncpg")


class Security(BaseSettings):
    model_config = ConfigDict(env_prefix="SECURITY_", env_file=ENV_FILE_PATH)

    key: str


class Config(BaseSettings):
    model_config = ConfigDict(env_file=ENV_FILE_PATH, extra="allow")

    app: AppSettings
    postgresql: PostgreSQL
    redis: Redis
    security: Security

    @classmethod
    def create(cls) -> "Config":
        return Config(
            app=AppSettings(),
            postgresql=PostgreSQL(),
            redis=Redis(),
            security=Security(),
        )
