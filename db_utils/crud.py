from .db import async_session
from sqlalchemy.future import select
import random
import string

from . import models, schemas

async def get_user(db: async_session, email: str, password: str):
    async with db as session:
        q = select(models.User).where(models.User.email == email, models.User.hashed_password == password + 'yeahhased')
        r = await session.execute(q)
        await db.close()
    response = r.scalars().first()
    return response

async def get_user_by_email(db: async_session, email: str):
    async with db as session:
        q = select(models.User).where(models.User.email == email)
        r = await session.execute(q)
        await db.close()
    response = r.scalars().first()
    return response

async def get_user_by_token(db: async_session, token: str):
    async with db as session:
        q = select(models.User).where(models.User.user_token == token)
        r = await session.execute(q)
        await db.close()
    response = r.scalars().first()
    return response

async def edit_user(db: async_session, user: schemas.UserEdit):
    fake_hashed_password = user.password + "yeahhased"
    user_token = ''.join(random.choice(string.ascii_letters) for i in range(16))
    user.password = fake_hashed_password
    async with db as session:
        q = select(models.User).where(models.User.user_token == user.user_token)
        db_user = await session.execute(q)
        db_user = db_user.scalars().first()
        for var, value in vars(user).items():
            setattr(db_user, var, value) if value else None
        await session.commit()
        await session.refresh(db_user)
    return {'user': db_user, 'token': user_token}

async def delete_user(db: async_session, user: schemas.UserDelete):
    async with db as session:
        q = select(models.User).where(models.User.user_token == user.user_token)
        db_user = await session.execute(q)
        db_user = db_user.scalars().first()

        await session.delete(db_user)
        await session.commit()
    return None

async def create_user(db: async_session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "yeahhased"
    user_token = ''.join(random.choice(string.ascii_letters) for i in range(16))
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password, user_token=user_token)
    async with db as session:
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)
    return {'user': db_user,'token':user_token}

async def get_documents(db: async_session, user_token:str):
    async with db as session:
        user = await get_user_by_token(session, user_token)
        q = select(models.Document).where(models.Document.owner_id == user.id)
        r = await session.execute(q)
    response = r.scalars().all()
    return response

async def create_user_document(db: async_session, item: schemas.DocumentCreate, db_user: models.User):
    async with db as session:
        # user = await get_user_by_token(session, user_token)
        db_document = models.Document(**item.dict(), owner_id=db_user.id)
        session.add(db_document)
        await session.commit()
        await session.refresh(db_document)
    return db_document

async def edit_user_document(db: async_session, item: schemas.DocumentEdit):
    async with db as session:
        q = select(models.Document).where(models.Document.id == item.document_id)
        d = await session.execute(q)
        document = d.scalars().first()
        if document is None:
            return None
        for var, value in vars(item).items():
            setattr(document, var, value) if value else None

        await session.commit()
        await session.refresh(document)
    return document

async def delete_document(db: async_session, item: schemas.UserDelete):
    async with db as session:
        q = select(models.Document).where(models.Document.id == item.document_id)
        d = await session.execute(q)
        document = d.scalars().first()
        if document is None:
            return None

        await session.delete(document)
        await session.commit()
    return None