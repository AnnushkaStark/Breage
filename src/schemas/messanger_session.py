from pydantic import BaseModel

from src.constants.enums import MessengerType


class MessangerSessionBase(BaseModel):
    messenger: MessengerType
    account_identifier: str
    session_data: dict
    is_active: bool
