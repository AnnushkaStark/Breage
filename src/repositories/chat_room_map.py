from sqlalchemy.ext.asyncio import AsyncSession

from src.models import ChatRoomMap
from src.repositories import RepositoryBase


class ChatRoomMapRepository(RepositoryBase):
    def __init__(self, session: AsyncSession):
        super().__init__(session, ChatRoomMap)
