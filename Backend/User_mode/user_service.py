
from User_mode.user_models import User
import User_mode.user_schemas as schemas
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

async def get_user_by_email(email: str, session: AsyncSession):
    query = select(User).where(User.email == email)
    result = await session.execute(query)
    return result.scalars().first()

async def create_user(user: schemas.UserCreate, session: AsyncSession):
    db_user = User(
        email=user.email,
        password=user.password,
        login=user.login
    )
    session.add(db_user)  # Добавляем пользователя в сессию
    await session.commit()  # Коммитим изменения
    await session.refresh(db_user)  # Обновляем объект, чтобы получить его ID
    return schemas.User(**user.model_dump(), id=db_user.id)

