from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import new_session
from Role_mode import role_schemas
from Role_mode import role_service

router = APIRouter()



@router.post("/", response_model=role_schemas.RoleGet)
async def create_role(role: role_schemas.RoleCreate):
    
    async with new_session() as session:  
        
        created_role = await role_service.create_role(role, session)  
        return created_role

@router.post("/add_role", response_model=role_schemas.RoleAdd)
async def add_role(role: role_schemas.RoleAdd):
    
    async with new_session() as session:  
        
        created_role = await role_service.add_role(role, session)  
        return created_role




