from pydantic import BaseModel


class MessageLogBase(BaseModel):
    sender_name: str
    text_content: str
    is_outbound: bool
    room_map_id: int
