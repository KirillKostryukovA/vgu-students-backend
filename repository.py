from sqlalchemy import select, update, delete

from database.database import SessionDep
from database.models import StudentData
from schemas.schema import SStudentAdd, SStudentUpdate

# Класс, в котором хранятся все запросы в бд
class StudentRepository():
    @classmethod
    async def get_students(cls, session: SessionDep):
        """ Получаем данные о всех пользователях """
        result = await session.execute(select(StudentData))

        return result.scalars().all()

    @classmethod
    async def get_user_data(cls, student_id: int, session: SessionDep):
        """ Получаем информацию об определённом пользователе """
        result = await session.execute(select(StudentData).where(StudentData.id==student_id))

        return result.scalar_one_or_none()

    @classmethod
    async def add_student(cls, session: SessionDep, student: SStudentAdd):
        """ Добавляем студента в базу данных """
        student_dict = student.model_dump()

        result = StudentData(**student_dict)

        # Добавляем студента в базу данных 
        session.add(result)
        await session.commit()
        await session.refresh(result)

        # Возвращаем результат
        return result

    @classmethod
    async def update_student_data(cls, student_id: int, session: SessionDep, student: SStudentUpdate):
        """ Обновляем данные пользователя """
        student_dict = student.model_dump(exclude_unset=True)

        stmt = await session.execute(
            update(StudentData)
            .where(StudentData.id==student_id)
            .values(**student_dict)
            .returning(StudentData))
        await session.commit()

        return stmt.scalar_one_or_none()

    @classmethod
    async def update_user(cls, student_id: int, session: SessionDep, student: SStudentAdd):
        """ Полностью обновляем все данные пользователя """
        student_dict = student.model_dump()

        stmt = await session.execute(
            update(StudentData).where(StudentData.id==student_id).values(**student_dict).returning(StudentData)
        )
        await session.commit()

        return stmt.scalar_one_or_none()

    @classmethod
    async def delete_user(cls, student_id: int, session: SessionDep):
        """ Удаляем пользователя из базы данных """
        await session.execute(
            delete(StudentData).where(StudentData.id==student_id)
        )
        await session.commit()

        return None