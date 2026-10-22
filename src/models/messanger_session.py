from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from databases.pg import Base
from src.constants.enums import MessengerType


class MessengerSession(Base):
    """
    Модель сессий мессенджера

    Attrs:
      - id: int - идентфикатор
      - messenger: MessengerType - тип месенджера
      - account_identifier: str - идентификатор аккаунта
      - session_data: dict - данные сессии
      - is_active: bool - сессия активна или нет
      - updated_at: datetime - дата и время обновления
    """

    __tablename__ = "messenger_session"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, unique=True, index=True
    )
    messenger: Mapped[ENUM] = mapped_column(
        ENUM(MessengerType, create_type=False)
    )
    account_identifier: Mapped[str] = mapped_column(String(100), unique=True)
    session_data: Mapped[dict] = mapped_column(JSONB)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
