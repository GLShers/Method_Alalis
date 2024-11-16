from typing import List, Optional
from pydantic import BaseModel



class CompanyCreate(BaseModel):
        
        title: str
        description: str
        owner_user_id: int  # ID владельца компании
class CompanyGet(CompanyCreate):
        id:int
        

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str
    login: str
    company:Optional[int] = None 
    my_company:Optional[int] = None 
    class Config:
        orm_mode = True

class User(UserBase):
    id: int
    

    class Config:
        orm_mode = True
