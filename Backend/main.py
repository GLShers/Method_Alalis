
from fastapi import FastAPI
from database import create_tables, delete_tables
from contextlib import asynccontextmanager

from User_mode.user_router import router as user_router
from Company_mode.company_router import router as company_router
from Role_mode.role_router import router as role_router




#----------------of-static--------------------------------
@asynccontextmanager
async def lifespan(app:FastAPI):
    
    await create_tables()
    yield
app = FastAPI(lifespan=lifespan)
#-------------------------------------------------




app.include_router(user_router, tags=["users"])
app.include_router(role_router, prefix="/role", tags=["role"])




