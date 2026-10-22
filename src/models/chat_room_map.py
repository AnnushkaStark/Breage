from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from databases.pg import Base
from src.constants.enums import MessengerType


class ChatRoomMap(Base):
    """
    Модель комнтат матрикс

    ## Attrs:
      - id: int - идентификатор
      - matrix_room_id: str - идентификатор комнаты в матрикс
      - external_chat_id: str - идентификатор чата
      - messenger:  MessengerType - тип мессенжера
      - chat_title: str - название чата
      - created_at: datetime - дата и время создания
    """

    __tablename__ = "chat_room_map"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, unique=True, index=True
    )
    matrix_room_id: Mapped[str] = mapped_column(String(255), unique=True)
    external_chat_id: Mapped[str] = mapped_column(String(100), index=True)
    messenger: Mapped[ENUM] = mapped_column(
        ENUM(MessengerType, create_type=False)
    )
    chat_title: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
