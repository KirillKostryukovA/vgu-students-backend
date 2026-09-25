from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass


engine = create_async_engine("sqlite+aiosqlite:///database.db")

async_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


# Зависимость, позволяющая получать доступ к сессии
async def get_db():
    async with async_session() as session:
        yield session


# Создаём аннотацию типа, 
SessionDep = Annotated[AsyncSession, Depends(get_db)]