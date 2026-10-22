from src.commons.tg_client import telegram_client
from src.constants.enums import MessengerType
from src.repositories.messanger_session import MessangerSessionRepository
from src.schemas.messanger_session import MessangerSessionBase
from src.schemas.messanger_session import TgCode
from src.services import ServiceBase


class MessangerSessionService(ServiceBase):
    def __init__(self, repository: MessangerSessionRepository):
        super().__init__(repository)

    async def create_session(self, schema: TgCode) -> MessangerSessionBase:
        session_data = await telegram_client.check_auth_code(schema=schema)
        return await self.manage_obj(
            action="create",
            schema=MessangerSessionBase(
                messenger=MessengerType.TELEGRAM,
                is_active=True,
                account_identifier=session_data["user_id"],
                session_data=session_data,
            ),
        )
