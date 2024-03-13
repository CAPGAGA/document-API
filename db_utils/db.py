from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.orm import sessionmaker

import os

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USERNAME = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB = os.getenv('POSTGRES_DB')

# engine
if all([DB_HOST, DB_PORT, DB_USERNAME, DB_PASSWORD, DB]):
    DATABASE_URL = f'postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB}'
else:
    DATABASE_URL = f'postgresql+asyncpg://postgres:postgres123@127.0.0.1:5432/dev'
print(DATABASE_URL)
engine = create_async_engine(DATABASE_URL, echo=True, future=True)
# base
Base: DeclarativeMeta = declarative_base()
# async session
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False, future=True)

async def get_db():
    db = async_session()
    try:
        yield db
    finally:
        await db.close()