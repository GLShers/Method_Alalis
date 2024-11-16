from typing import List
from fastapi import FastAPI, HTTPException
from database import async_engine, create_tables, delete_tables, new_session
from contextlib import asynccontextmanager
import crud
import schemas

@asynccontextmanager
async def lifespan(app:FastAPI):
    await delete_tables()
    await create_tables()
    print("Create")
    yield
    print("Off")



app = FastAPI(lifespan=lifespan)





@app.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate):

    async with new_session() as session:  # Создаем сессию

        db_user = await crud.get_user_by_email(email=user.email, session=session)  # Передаем сессию

        if db_user:

            raise HTTPException(status_code=400, detail="Email already registered")

        return await crud.create_user(user=user, session=session) 

@app.post("/company/", response_model=schemas.CompanyGet)
async def create_company(company: schemas.CompanyCreate):
    # Проверяем, существует ли компания с таким же заголовком
    async with new_session() as session:  
        db_company = await crud.get_company_by_title(title_a=company.title, session=session)
        if db_company:
            raise HTTPException(status_code=409, detail="Company with this title already exists.")
        
        # Создаем новую компанию
        created_company = await crud.create_company(company=company, session=session)  

        # Возвращаем созданную компанию, преобразованную в схему
        return schemas.CompanyGet(**created_company.model_dump())
