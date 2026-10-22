from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from databases.pg import Base


class Admin(Base):
    """
    Модель пользвателя -админа

    ## Attrs:
      - id: int - идентификатор
      - email: str - почта
      - password: str - пароль
    """

    __tablename__ = "admin"
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, unique=True, index=True
    )
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100), index=True)
