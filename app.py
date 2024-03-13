from fastapi import FastAPI
import asyncio

from db_utils import models
from db_utils.db import async_session, engine

import logging

from api_routers import users, documents

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(documents.router)
app.include_router(users.router)


@app.on_event('startup')
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

async def get_db():
    db = async_session()
    try:
        yield db
    finally:
        db.close()




