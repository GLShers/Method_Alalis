from Role_mode.role_model import Role
import Role_mode.role_schemas as schemas
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from User_mode.user_models import User
from User_mode.user_schemas import GetUser

async def create_role(role: schemas.RoleCreate, session: AsyncSession):
    db_role = Role(
        title=role.title,
        description=role.description,
    )
    session.add(db_role)  # Добавляем компанию в сессию
    await session.commit()  # Коммитим изменения
    await session.refresh(db_role)  # Обновляем объект, чтобы получить его ID
    return schemas.RoleGet(**role.model_dump(), id= db_role.id)


async def add_role(user:schemas.RoleAdd, session: AsyncSession):#вставляем title и id юзера
    result = await session.execute(select(User).where(User.id == user.user_id))#ищем
    user_instance = result.scalars().first()#получаем первого пользователя с таким айди
    if user_instance:
        result_role = await session.execute(select(Role).where(Role.title == user.title))#ищем
        role_instance = result_role.scalars().first()#получаем первого пользователя с таким айди
        if role_instance:
            user_instance.role_id = role_instance.id
            await session.commit()  # Коммитим изменения
            await session.refresh(user_instance)  # Обновляем объект, чтобы получить его ID
            return schemas.RoleAdd(title=user.title, user_id=user.user_id)
        raise HTTPException(status_code=401, detail="Role not found")
    raise HTTPException(status_code=401, detail="User not found")
     


