from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db_session

from User_mode import user_schemas
from User_mode import user_service

router = APIRouter()


@router.post("/", response_model=user_schemas.GetUser)
async def create_user(user: user_schemas.UserCreate, session: AsyncSession = Depends(get_db_session)):

    return await user_service.create_user(user=user, session=session) 
    
    
""" @router.get("/{id}", response_model=user_schemas.UserResponse)
async def get_user(id: int):
    async with new_session() as session:  # Создаём сессию
        user = await user_service.get_user(id=id, session=session)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    
@router.post("/sign_in", response_model=user_schemas.GetUser)
async def sign_in(user:user_schemas.Sign_in):
    async with new_session() as session:  # Создаём сессию
        login=user.login
        user = await user_service.sign_in(user, session=session)
        if not user:
            raise HTTPException(status_code=404, detail=f"Пользователь с логином '{login}' не существует.")
        return user """