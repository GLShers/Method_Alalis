import bcrypt
from User_mode.user_models import User
import User_mode.user_schemas as schemas
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from fastapi  import HTTPException

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

async def get_user(id:int , session: AsyncSession):
    query = (
        select(User)
        .options(joinedload(User.role), joinedload(User.task))  # Подгружаем связи
        .where(User.id == id)
    )
    result = await session.execute(query)
    user_obj = result.scalars().first()  # Получаем первого пользователя
    return user_obj  # Возвращаем объект User

async def sign_in(user:schemas.Sign_in , session: AsyncSession):
    login=user.login
    password=user.password
    query_login = (select(User).where(User.login == login))
    query_password=(select(User).where(User.password==password))
    result = await session.execute(query_login)
    user_obj = result.scalars().first()  # Получаем первого пользователя
    if user_obj:
        if bcrypt.checkpw(password.encode('utf-8'), user_obj.password.encode('utf-8')):
            return user_obj  # Возвращаем объект User
        raise HTTPException(status_code=404, detail=f"Неверный пароль")
    raise HTTPException(status_code=404, detail=f"Пользователь с логином '{login}' не существует.")


""" async def get_user(user: schemas.GetUser , session: AsyncSession):
    query = select(User).where(User.login == user.login)
    result = await session.execute(query)
    return result.scalars().first() 
 """