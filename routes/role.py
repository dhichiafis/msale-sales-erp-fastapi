from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from models.model import *
from models.schema import *

from typing import List
roles_router=APIRouter(prefix='/roles',tags=['roles'])

@roles_router.get('/all',response_model=List[RoleBase])
async def get_all_roles(db:Session=Depends(connect)):
    roles=db.query(Role).all()
    return roles 


@roles_router.get('/{id}',response_model=RoleBase)
async def get_role(id:int ,db:Session=Depends(connect)):
    role=db.query(Role).filter(Role.id==id).first()
    return role 