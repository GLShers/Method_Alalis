import bcrypt
from User_mode.user_models import User
import User_mode.user_schemas as schemas
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

""" async def get_user_by_email(email: str, session: AsyncSession):
    query = select(User).where(User.email == email)
    result = await session.execute(query)
    return result.scalars().first() """ 

async def create_user(user: schemas.UserCreate, session: AsyncSession):
    # Хешируем пароль
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())#перевод в байты

    db_user = User(
        password=hashed_password.decode('utf-8'),  # Сохраняем хешированный пароль
        login=user.login,
        company=user.company
    )
    session.add(db_user)  # Добавляем пользователя в сессию
    await session.commit()  # Коммитим изменения
    await session.refresh(db_user)  # Обновляем объект, чтобы получить его ID
    return schemas.GetUser(**user.model_dump(), id=db_user.id)

async def get_user(user: schemas.GetUser , session: AsyncSession):
    query = select(User).where(User.login == user.login)
    result = await session.execute(query)
    return result.scalars().first() 
