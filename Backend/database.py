from sqlalchemy import Engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from dotenv import load_dotenv #
import os #для работы с переменными окружения

load_dotenv()
DATABASE_URL =os.getenv('DATABASE_URL')


# Создание асинхронного движка
async_engine = create_async_engine(DATABASE_URL, echo=True)
# Создание асинхронной сессии
AsyncSessionLocal = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)


async def get_db_session():

    async with AsyncSessionLocal() as session:

        yield session
#определяем класс для создания моделей
class Model(DeclarativeBase): 
    pass

# Определение функций для создания и удаления таблиц
async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

async def delete_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)