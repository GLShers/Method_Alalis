from typing import List, Optional
from pydantic import BaseModel


class RoleCreate(BaseModel):
        
        title: str
        description: str
        class Config:
                orm_mode = True

        
class RoleGet(RoleCreate):
        id:int
        

class RoleAdd(BaseModel):
        
        title: str
        user_id: int
        class Config:
                orm_mode = True

       