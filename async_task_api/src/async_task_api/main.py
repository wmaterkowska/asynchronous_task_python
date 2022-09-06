import asyncio

import uvicorn as uvicorn
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from async_task_api.src.async_task_api import crud, schema
from async_task_api.src.async_task_api.database import init_models

# model.Base.metadata.create_all(bind=engine)

app = FastAPI()

"""
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
"""


@app.post("/tasks", response_model=schema.Task)
async def create_task(session: AsyncSession, task: schema.TaskCreate):
    new_task = crud.create_task(session, task.base, task.exponent)
    await session.commit()
    return new_task


@app.get("/tasks", response_model=list[schema.Task])
async def get_tasks(session: AsyncSession):
    tasks = await crud.get_tasks(session)
    return [schema.Task(id=t.id, base=t.base, exponent=t.exponent, status=t.status, result=t.result) for t in tasks]


"""
@app.get("/tasks/{task_id}", response_model=schema.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.TaskCRUD.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task
"""

if __name__ == "__main__":
    asyncio.run(init_models())
    uvicorn.run("async_task_api.src.async_task_api.main:app", port=8000, host='127.0.0.1')
