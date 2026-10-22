from pydantic import BaseModel

from src.constants.enums import MessengerType


class ChatRoomMapBase(BaseModel):
    matrix_room_id: str
    xternal_chat_id: str
    messenger: MessengerType
    chat_title: str
