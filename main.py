from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from routers.router import rout as stu_router
from database.models import StudentData
from database.database import engine, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    print("Запуск программы")

    yield

    print("Выключение сервера")


app = FastAPI(lifespan=lifespan)
app.include_router(stu_router)


# Запуск программы
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)