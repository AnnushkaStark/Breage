from sqlalchemy.ext.asyncio import AsyncSession

from src.models import MessengerSession
from src.repositories import RepositoryBase


class MessangerSessionRepository(RepositoryBase):
    def __init__(self, session: AsyncSession):
        super().__init__(session, MessengerSession)
