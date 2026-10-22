from sqlalchemy.ext.asyncio import AsyncSession

from src.models import MessageLog
from src.repositories import RepositoryBase


class MessageLogRepository(RepositoryBase):
    def __init__(self, session: AsyncSession):
        super().__init__(session, MessageLog)
