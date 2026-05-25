from app.core.db import SessionLocal, Base
from app.core.db_async import AsyncSessionLocal


# Synchronous
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Async
async def get_db():
    async with AsyncSessionLocal() as db:
        yield db
