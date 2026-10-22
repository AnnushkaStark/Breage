from pathlib import Path

from .base import BaseSetting

BASE_DIR = Path(__file__).parent.parent


class DBSettings(BaseSetting):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str


class RedisSettings(BaseSetting):
    HOST: str = "redis"
    PORT: int = 6379
    REDIS_URL: str = "redis://redis:6379/0"


redis_settings = RedisSettings()
db_settings = DBSettings()
