from fastapi import APIRouter
from fastapi import status

from src.api.depends.messanger_session import MessangerSessionServiceDepends
from src.commons.tg_client import telegram_client
from src.constants.errors import ErrorCodes
from src.schemas.messanger_session import TgAuthCodeRequest
from src.schemas.messanger_session import TgCode
from src.utils.errors import errs

router = APIRouter()


@router.post(
    "/",
    status_code=status.HTTP_200_OK,
    responses=(_tg_auth_err := errs(e400=ErrorCodes.ALREADY_AUTHENTICTAED)),
)
async def send_code_response(schema: TgAuthCodeRequest):
    return await telegram_client.get_auth_code(schema=schema)


@router.post(
    "/tg/check_code/", status_code=status.HTTP_200_OK, responses=_tg_auth_err
)
async def check_auth_code(
    service: MessangerSessionServiceDepends, schema: TgCode
):
    return await service.create_session(schema=schema)
