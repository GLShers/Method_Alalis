from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from database import new_session

from User_mode import user_schemas
from User_mode import user_service

router = APIRouter()


@router.post("/", response_model=user_schemas.GetUser)
async def create_user(user: user_schemas.UserCreate):

    async with new_session() as session:  # Создаем сессию

        return await user_service.create_user(user=user, session=session) 
    
    
    
""" @router.post("/", response_model=user_schemas.GetUser)
async def get_user(user: user_schemas.GetUser):

    async with new_session() as session:  # Создаем сессию

        return await user_service.get_user(user=user, session=session) 
    
 """