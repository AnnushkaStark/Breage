from typing import Annotated

from fastapi import Depends

from src.api.depends import Session
from src.repositories.messanger_session import MessangerSessionRepository
from src.services.messanger_session import MessangerSessionService


def get_messanger_session_repository(
    session: Session,
) -> MessangerSessionRepository:
    return MessangerSessionRepository(session=session)


MessangerSessionRepositoryDepends = Annotated[
    MessangerSessionRepository, Depends(get_messanger_session_repository)
]


def get_massnger_session_service(
    repository: MessangerSessionRepositoryDepends,
) -> MessangerSessionService:
    return MessangerSessionService(repository=repository)


MessangerSessionServiceDepends = Annotated[
    MessangerSessionService, Depends(get_massnger_session_service)
]
