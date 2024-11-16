from typing import List, Optional
from pydantic import BaseModel


class RoleCreate(BaseModel):
        
        title: str
        description: str
        
class RoleGet(RoleCreate):
        id:int
        

