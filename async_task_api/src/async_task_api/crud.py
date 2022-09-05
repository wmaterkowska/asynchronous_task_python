from sqlalchemy.orm import Session

from . import model, schema


def get_task(db: Session, task_id: int):
    return db.query(model.Task).filter(model.Task.id == task_id).first()


def get_tasks(db: Session):
    return db.query(model.Task).all()


def create_task(db: Session, task: schema.TaskCreate):
    db_task = model.Task(base=task.base, exponent=task.exponent, status=0, result=0)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
