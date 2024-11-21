""" from Company_mode.company_model import Company
import User_mode.user_schemas as schemas
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

async def create_company(company: schemas.CompanyCreate, session: AsyncSession):
    db_company = Company(
        title=company.title,
        description=company.description,
        owner_user_id=company.owner_user_id
    )
    session.add(db_company)  # Добавляем компанию в сессию
    await session.commit()  # Коммитим изменения
    await session.refresh(db_company)  # Обновляем объект, чтобы получить его ID
    return schemas.CompanyGet(**company.model_dump(), id=db_company.id)


 """