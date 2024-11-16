from typing import List
from fastapi import FastAPI, HTTPException
from database import async_engine, create_tables, delete_tables, new_session
from contextlib import asynccontextmanager

from User_mode.user_router import router as user_router
from Company_mode.company_router import router as company_router

@asynccontextmanager
async def lifespan(app:FastAPI):
    await delete_tables()
    await create_tables()
    print("Create")
    yield
    print("Off")
    
app = FastAPI(lifespan=lifespan)
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(company_router, prefix="/company", tags=["company"])




