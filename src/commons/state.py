import json
from typing import Any

from redis.asyncio.lock import Lock

from src.databases.redis_db import get_redis


class State:
    def _deserialize(self, data: bytes) -> Any:
        decoded_str = data.decode("utf-8")
        try:
            return json.loads(decoded_str)
        except (json.JSONDecodeError, TypeError):
            return decoded_str

    def _serialize(self, data: Any) -> str:
        if data is None:
            return ""

        if isinstance(data, str):
            return data

        try:
            return json.dumps(data, ensure_ascii=False)
        except (TypeError, ValueError):
            return str(data)

    async def set_state(self, key: str, value: Any, ttl: int = 600) -> None:
        async with get_redis() as redis:
            await redis.set(
                name=key, ex=ttl, value=self._serialize(data=value), nx=True
            )

    async def get_state(self, key: str) -> str | None:
        async with get_redis() as redis_client:
            if found_obj := await redis_client.get(key):
                await redis_client.delete(key)
                return self._deserialize(found_obj)

            lock_key = f"{key}:lock"
            async with Lock(
                redis_client, lock_key, timeout=10, blocking_timeout=15
            ):
                if found_obj := await redis_client.get(key):
                    return self._deserialize(found_obj)


state = State()
