from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db_utils.db import get_db
from db_utils import schemas, crud

router = APIRouter(
    prefix="/user",
    tags=["users"],
)

@router.get("/mail/{email}/{password}")
async def get_user(email: str, password: str, db: Session = Depends(get_db)):
    db_user = await crud.get_user(db, email, password)
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return db_user

@router.get("/token/{user_token}")
async def get_user_by_token(user_token:str, db: Session = Depends(get_db)):
    db_user = await crud.get_user_by_token(db, token=user_token)
    # if db_user is None:
    #     raise HTTPException(status_code=400, detail='You are not registered')
    return db_user

@router.post("/")
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = await crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail='User already exists')
    return await crud.create_user(db, user)

@router.put("/")
async def edit_user(user: schemas.UserEdit, db: Session = Depends(get_db)):
    db_user = await crud.get_user_by_token(db, user.user_token)
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return await crud.edit_user(db, user)

@router.delete("/")
async def delete_user(user: schemas.UserDelete, db: Session = Depends(get_db)):
    db_user = await crud.get_user_by_token(db, user.user_token)
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return await crud.delete_user(db, user)

