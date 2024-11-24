from typing import List, Optional
from pydantic import BaseModel
from Role_mode.role_schemas import RoleGet



class GetUser(BaseModel):
    id: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    password: str
    login: str
    company:int
    class Config:
        orm_mode = True

class UserResponse(UserCreate):
    id:int
    role_id:int
    role: RoleGet  # Связанная модель Role
   
    class Config:
        orm_mode = True

