from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from database import new_session

from Role_mode import role_schemas
from Role_mode import role_service

router = APIRouter()



@router.post("/", response_model=role_schemas.RoleGet)
async def create_role(role: role_schemas.RoleCreate):
    
    async with new_session() as session:  
        
        created_role = await role_service.create_role(role=role, session=session)  
        return created_role


