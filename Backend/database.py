from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import Column, Integer, String, Float
from dotenv import load_dotenv #
import os #для работы с переменными окружения
load_dotenv()


DATABASE_URL =os.getenv('DATABASE_URL')

# Создание асинхронного движка
async_engine = create_async_engine(DATABASE_URL, echo=True)

# Создание асинхронной сессии
new_session = async_sessionmaker(async_engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

# Определение модели
async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

async def delete_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)