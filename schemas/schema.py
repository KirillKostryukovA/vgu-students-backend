from enum import Enum

from pydantic import BaseModel, Field, ConfigDict


# Создаём перечисления для обозначения формы обучения студента/тки
class form_learning(str, Enum):
    full_time = "очная"
    part_time = "заочная"


# Основной класс для валидации данных
class SStudent(BaseModel):
    surname: str
    name: str
    otchestvo: str | None = Field(None, max_length=20)
    faculty: str = Field(max_length=8)
    learning_form: form_learning


# Класс для чтения данных
class SStudentRead(SStudent):
    id: int

    # Включаем ORM-поддержку
    model_config = ConfigDict(from_attributes=True)


# Класс для добавления нового студента в бд
class SStudentAdd(SStudent):
    number_id: int


# Класс для обновления данных студента
class SStudentUpdate(BaseModel):
    surname: str | None = None
    name: str | None = None
    otchestvo: str | None = Field(None, max_length=20)
    faculty: str | None = Field(None, max_length=8)
    learning_form: form_learning | None = None
    number_id: int | None = None