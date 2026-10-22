from sqlalchemy.ext.asyncio import AsyncSession

from src.models import SystemAlertLog
from src.repositories import RepositoryBase


class SystemAlertLogRepository(RepositoryBase):
    def __init__(self, session: AsyncSession):
        super().__init__(session, SystemAlertLog)
