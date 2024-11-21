from typing import List, Optional
from pydantic import BaseModel




class GetUser(BaseModel):
    id: int
    login: str
    

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    password: str
    login: str
    company:int
    class Config:
        orm_mode = True

