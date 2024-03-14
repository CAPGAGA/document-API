from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db_utils.db import get_db
from db_utils import schemas, crud

router = APIRouter(
    prefix="/documents",
    tags=["documents"],
)


@router.post('/{user_token}', status_code=201)
async def create_document(user_token:str, document:schemas.DocumentCreate, db: Session = Depends(get_db)):
    db_user = await crud.get_user_by_token(db, token=user_token)
    if db_user is None:
        raise HTTPException(status_code=404, detail='You are not registered')
    return await crud.create_user_document(db, document, db_user)


@router.get('/{user_token}', status_code=200)
async def get_documents(user_token:str, db: Session = Depends(get_db)):
    db_user = await crud.get_user_by_token(db, token=user_token)
    if db_user is None:
        raise HTTPException(status_code=404, detail='User with that token is not found')
    return await crud.get_documents(db, user_token)

@router.put('/', status_code=201)
async def edit_document(document: schemas.DocumentEdit, db: Session = Depends(get_db)):
    db_user = await crud.get_user_by_token(db, token=document.user_token)
    if db_user is None:
        raise HTTPException(status_code=404, detail='User with that token is not found')

    response = await crud.edit_user_document(db, document)
    if response is None:
        return HTTPException(status_code=404, detail='Document is not found')
    return response

@router.delete('/', status_code=204)
async def delete_document(document: schemas.DocumentDelete, db: Session = Depends(get_db)):
    db_user = await crud.get_user_by_token(db, token=document.user_token)
    if db_user is None:
        raise HTTPException(status_code=404, detail='User with that token is not found')
    response = await crud.delete_document(db, document)
    return response