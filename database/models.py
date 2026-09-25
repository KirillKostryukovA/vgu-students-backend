from enum import Enum

from sqlalchemy import String, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base


class form_learning_db(str, Enum):
    full_time = "очная"
    part_time = "заочная"


class StudentData(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    surname: Mapped[str]
    name: Mapped[str]
    otchestvo: Mapped[str | None] = mapped_column(String(20))
    faculty: Mapped[str] = mapped_column(String(8))
    learning_form: Mapped[form_learning_db] = mapped_column(SQLEnum(form_learning_db, name="form_learning"))
    number_id: Mapped[str]