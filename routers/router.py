from fastapi import APIRouter

from schemas.schema import SStudentAdd, SStudentRead, SStudentUpdate
from database.database import SessionDep
from database.models import StudentData
from repository import StudentRepository

# Роутер FastAPI
rout = APIRouter(
    prefix="/student",
    tags=["Студенчиские билеты"],
)


@rout.post("/", response_model=SStudentRead)
async def add_student(
    student: SStudentAdd,
    session: SessionDep,
):
    """ Добавляем студента в базу данных """
    result = await StudentRepository.add_student(session, student)
    return result


@rout.get("/", response_model=list[SStudentRead])
async def get_all_students(
    session: SessionDep,
):
    """ Получаем информацию о всех студентах """
    students = await StudentRepository.get_students(session)
    return students


@rout.get("/{student_id}")
async def get_user_data(
    student_id: int,
    session: SessionDep,
):
    """ Получаем информацию об определённом студенте """
    return await StudentRepository.get_user_data(student_id, session)


@rout.patch("/{student_id}", response_model=SStudentRead)
async def update_data_user(
    student_id: int,
    student: SStudentUpdate,
    session: SessionDep,
):
    """ Обновляем данные пользователя """
    return await StudentRepository.update_student_data(student_id, session, student)


@rout.put("/{student_id}", response_model=SStudentRead)
async def update_user(
    student_id: int,
    student: SStudentAdd,
    session: SessionDep
):
    """ Полностью обновляем данные пользователя """
    return await StudentRepository.update_user(student_id, session, student)


@rout.delete("/{student_id}")
async def delete_user(
    student_id: int,
    session: SessionDep,
):
    """ Полностью удаляем пользователя из базы данных """
    return await StudentRepository.delete_user(student_id, session)