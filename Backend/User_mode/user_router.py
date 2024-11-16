from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from database import new_session

from User_mode import user_schemas
from User_mode import user_service

router = APIRouter()


@router.post("/", response_model=user_schemas.User)
async def create_user(user: user_schemas.UserCreate):

    async with new_session() as session:  # Создаем сессию

        db_user = await user_service.get_user_by_email(email=user.email, session=session)  # Передаем сессию

        if db_user:

            raise HTTPException(status_code=400, detail="Email already registered")

        return await user_service.create_user(user=user, session=session) 