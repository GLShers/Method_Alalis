""" from typing import List, Optional
from pydantic import BaseModel


class CompanyCreate(BaseModel):
        
        title: str
        description: str
        owner_user_id: int  # ID владельца компании
class CompanyGet(CompanyCreate):
        id:int
        

 """