from Task_mode.task_model import Task
from Task_mode import task_schemas as schemas
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

async def create_task(task: schemas.TaskCreate, session: AsyncSession):
     # Удаляем информацию о временной зоне из даты

    naive_date = task.date.replace(tzinfo=None, microsecond=0)
    
    db_task = Task(
        name_task=task.name_task,
        description_task=task.description_task,
        date=naive_date,
        complexity= task.complexity,
        owner_user_id=task.owner_user_id
    )
    session.add(db_task)  # Добавляем компанию в сессию
    await session.commit()  # Коммитим изменения
    await session.refresh(db_task)  # Обновляем объект, чтобы получить его ID
    return db_task

""" async def get_company_by_title(title_a: str, session: AsyncSession):

    result = await session.execute(select(Company).where(Company.title == title_a))  # Выполнение запроса
    company = result.scalars().first()  # Извлечение первой найденной компании
    if company:  # Если компания найдена
        raise HTTPException(status_code=409, detail=f"Компания с названием '{title_a}' уже существует.")
    return None  # Если компания не найдена, возвращаем None
 """