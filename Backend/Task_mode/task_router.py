from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import AsyncSessionLocal
from Task_mode import task_schemas as schemas
from Task_mode import task_service as service

router = APIRouter()

@router.post("/", response_model=schemas.TaskGet)
async def create_task(task: schemas.TaskCreate):
    # Проверяем, существует ли компания с таким же заголовком
    async with AsyncSessionLocal() as session:  
        # Создаем новую компанию
        created_task = await service.create_task(task=task, session=session)  

        # Возвращаем созданную компанию, преобразованную в схему
        return created_task 