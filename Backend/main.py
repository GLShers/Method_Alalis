from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from typing import List
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse 
from database import async_engine, create_tables, delete_tables, new_session
from contextlib import asynccontextmanager

from User_mode.user_router import router as user_router
from Company_mode.company_router import router as company_router

@asynccontextmanager
async def lifespan(app:FastAPI):
    
    await create_tables()
    print("Create")
    yield
    print("Off")
app = FastAPI(lifespan=lifespan)

templates_dir = Path(__file__).parent.parent / "Front"  
templates_dir_up= Path(__file__).parent.parent / "Front" 

templates = Jinja2Templates(directory=templates_dir_up)

app.mount("/css", StaticFiles(directory=templates_dir / "css"), name="css")

app.mount("/photo", StaticFiles(directory=templates_dir / "photo"), name="photo")
app.mount("/video.mp4", StaticFiles(directory=templates_dir), name="video")  # Для видео

app.mount("/log_out.html", StaticFiles(directory=templates_dir), name="log_out")  # Для log_out.html

app.mount("/favicon.ico", StaticFiles(directory=templates_dir), name="favicon")  # Для favicon


@app.get("/", response_class=HTMLResponse)

async def read_index(request: Request):

    return templates.TemplateResponse("log_out.html", {"request": request})


app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(company_router, prefix="/company", tags=["company"])




