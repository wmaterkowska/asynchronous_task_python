import time

from sqlalchemy.orm import Session

from . import model, schema


def get_task(db: Session, task_id: int):
    return db.query(model.Task).filter(model.Task.id == task_id).first()


def get_tasks(db: Session):
    return db.query(model.Task).all()


async def create_task(db: Session, task: schema.TaskCreate):

    db_task = model.Task(base=task.base, exponent=task.exponent, status=0, result=0)
    db.add(db_task)
    db.commit()
    db.add(db_task)
    db.refresh(db_task)

    current_result = 1
    for i in range(db_task.exponent):
        time.sleep(1)
        db_task.status = ((i / db_task.exponent) * 100)
        current_result = db_task.base * current_result
    db_task.result = current_result
    db_task.status = 100

    return db_task
