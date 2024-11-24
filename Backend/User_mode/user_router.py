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
    
    
@router.get("/{id}", response_model=user_schemas.UserResponse)
async def get_user(id: int):
    async with new_session() as session:  # Создаём сессию
        user = await user_service.get_user(id=id, session=session)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user