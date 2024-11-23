from typing import List, Optional
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskCreate(BaseModel):
        
        name_task: str
        descr_task: Optional[str]#необязательно
        date: datetime
        owner_user_id: int
        class Config:
                orm_mode = True

class TaskGet(TaskCreate):
        id:int
        

