""" from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from database import new_session

from Company_mode import company_schemas
from Company_mode import company_service

router = APIRouter()



@router.post("/", response_model=company_schemas.CompanyGet)
async def create_company(company: company_schemas.CompanyCreate):
    # Проверяем, существует ли компания с таким же заголовком
    async with new_session() as session:  
        db_company = await company_service.get_company_by_title(title_a=company.title, session=session)
        if db_company:
            raise HTTPException(status_code=409, detail="Company with this title already exists.")
        
        # Создаем новую компанию
        created_company = await company_service.create_company(company=company, session=session)  

        # Возвращаем созданную компанию, преобразованную в схему
        return company_schemas.CompanyGet(**created_company.model_dump())
 """