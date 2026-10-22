from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from databases.pg import Base


class MessageLog(Base):
    """
    Модель лога сообщений

    ## Attrs:
      - id: int - идентификатор
      - sender_name: str - имя пользователя
      -  text_content: str - текст сообщения
      - is_outbound: bool - это исходящее или нет
      - created_at: datetime - дата и время создания
    """

    __tablename__ = "message_log"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, unique=True, index=True
    )
    sender_name: Mapped[str] = mapped_column(String(100))
    text_content: Mapped[str] = mapped_column(Text)
    is_outbound: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    room_map_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("chat_room_map.id", ondelete="CASCADE")
    )
