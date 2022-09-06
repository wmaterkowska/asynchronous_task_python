from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from async_task_api.src.async_task_api import crud, model, schema
from async_task_api.src.async_task_api.database import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        print("test")
        db.close()


@app.post("/tasks/", response_model=schema.Task)
async def create_task(task: schema.TaskCreate, db: Session = Depends(get_db)):
    task_new = await crud.create_task(db=db, task=task)
    return task_new


@app.get("/tasks/", response_model=list[schema.Task])
async def read_tasks(db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db)
    return tasks

"""
@app.get("/tasks/{task_id}", response_model=schema.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task
"""

