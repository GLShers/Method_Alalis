
from fastapi import FastAPI
from database import create_tables, delete_tables
from contextlib import asynccontextmanager

from User_mode.user_router import router as user_router
from Role_mode.role_router import router as role_router
from Task_mode.task_router import router as task_router



#----------------of-static--------------------------------
@asynccontextmanager
async def lifespan(app:FastAPI):
    
    await create_tables()
    yield
app = FastAPI(lifespan=lifespan)
#-------------------------------------------------




app.include_router(user_router,prefix="/user", tags=["users"])
app.include_router(role_router,prefix="/role", tags=["role"])
app.include_router(task_router,prefix="/task", tags=["task"])




