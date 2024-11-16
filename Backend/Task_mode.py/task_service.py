from Company_mode.company_model import Company
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

async def get_company_by_title(title_a: str, session: AsyncSession):

    result = await session.execute(select(Company).where(Company.title == title_a))  # Выполнение запроса
    company = result.scalars().first()  # Извлечение первой найденной компании
    if company:  # Если компания найдена
        raise HTTPException(status_code=409, detail=f"Компания с названием '{title_a}' уже существует.")
    return None  # Если компания не найдена, возвращаем None
