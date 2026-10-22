from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Text
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from databases.pg import Base


class SystemAlertLog(Base):
    """
    Модель системных оповещений

    ## Attrs:
      - id: int - идентификатор
      - error_message: str - оповещение об ошибке
      - is_sent_to_email: bool - отправлено на емейл
      - created_at: datetime - дата и время создания
    """

    __tablename__ = "system_alert_log"

    id: Mapped[int] = mapped_column(primary_key=True)
    error_message: Mapped[str] = mapped_column(Text)
    is_sent_to_email: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
