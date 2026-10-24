from fastapi import APIRouter

from src.api.endpoints.messanger_session import (
    router as messanger_session_router,
)

api_router = APIRouter(prefix="/api")


api_router.include_router(
    messanger_session_router,
    prefix="/messanger_session",
    tags=["MessangerSession"],
)
