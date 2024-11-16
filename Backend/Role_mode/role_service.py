from Role_mode.role_model import Role
import Role_mode.role_schemas as schemas
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

async def create_role(role: schemas.RoleCreate, session: AsyncSession):
    db_role = Role(
        title=role.title,
        description=role.description,
    )
    session.add(db_role)  # Добавляем компанию в сессию
    await session.commit()  # Коммитим изменения
    await session.refresh(db_role)  # Обновляем объект, чтобы получить его ID
    return schemas.RoleGet(**role.model_dump(), id=db_role.id)


async def add_role(id:int, session: AsyncSession):
    session.add(id)  # Добавляем компанию в сессию
    await session.commit()  # Коммитим изменения
    await session.refresh(db_role)  # Обновляем объект, чтобы получить его ID
    return schemas.RoleGet(**role.model_dump(), id=db_role.id)


