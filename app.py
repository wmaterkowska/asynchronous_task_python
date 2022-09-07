import uvicorn
import asyncio
from fastapi import FastAPI

from db.config import engine, Base, async_session
from routers import task_router


app = FastAPI()
app.include_router(task_router.router)



@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == '__main__':
    asyncio.run(uvicorn.run("app:app", port=8000, host='127.0.0.1'))
