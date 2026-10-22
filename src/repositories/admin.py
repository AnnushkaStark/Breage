from sqlalchemy.ext.asyncio import AsyncSession

from src.models import Admin
from src.repositories import RepositoryBase


class AdminRepository(RepositoryBase):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Admin)
