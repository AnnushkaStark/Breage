from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from telethon import TelegramClient
from telethon.sessions import StringSession

from src.commons.state import state
from src.config.configs import tg_settings
from src.constants.errors import DomainError
from src.constants.errors import ErrorCodes
from src.schemas.messanger_session import TgAuthCodeRequest
from src.schemas.messanger_session import TgCode
from src.utils.logger import logger


class TelegramClient:
    def __init__(self):
        self.app_id = tg_settings.APP_ID
        self.app_secret = tg_settings.APP_SECRET
        self.session = None
        self.tg_client = None

    @asynccontextmanager
    async def _get_client(self) -> AsyncGenerator[TelegramClient, None]:
        logger.info("Инициализация клинета в телеграм")
        if not self.session:
            self.session = StringSession()

        if not self.tg_client:
            self.tg_client = TelegramClient(
                self.session, self.app_id, self.app_secret
            )

        if not self.tg_client.is_connected():
            await self.tg_client.connect()

        try:
            yield self.tg_client

        finally:
            if self.tg_client and self.tg_client.is_connected():
                await self.tg_client.disconnect()

    async def _check_authenticated(self) -> None:
        logger.info("Проверка аутентификации")
        async with self._get_client() as client:
            if await client.is_user_authorized():
                logger.warning("Клинет уже авторизован")
                raise DomainError(ErrorCodes.ALREADY_AUTHENTICTAED)

    async def get_auth_code(self, schema: TgAuthCodeRequest) -> None:
        logger.info("Получение кода аутентификации")
        async with self._get_client() as client:
            await self._check_authenticated()
            phone_code_hash = await client.send_code_request(
                phone=schema.phone
            )
            temp_session_str = client.session.save()

            payload = {
                "session_str": temp_session_str,
                "phone_code_hash": phone_code_hash.phone_code_hash,
            }

            await state.set_state(key=schema.phone, value=payload)

    async def check_auth_code(self, schema: TgCode) -> None:
        logger.info("Проврека кода аутентификации")
        cached_data = await state.get_state(key=schema.phone)
        if not cached_data:
            logger.warning("Код не найден")
            raise DomainError(ErrorCodes.AUTH_CODE_NOT_REQUESTED)

        temp_session_str = cached_data["session_str"]
        phone_code_hash = cached_data["phone_code_hash"]

        async with self._get_client() as client:
            await self._check_authenticated()
            client.session.load(temp_session_str)

        await client.sign_in(
            phone=schema.phone,
            code=schema.code,
            phone_code_hash=phone_code_hash,
        )

        final_session_str = client.session.save()
        return final_session_str


telegram_client = TelegramClient()
