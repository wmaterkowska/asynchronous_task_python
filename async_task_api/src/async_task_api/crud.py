import time

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from . import model, schema
from .model import Task


async def get_tasks(session: AsyncSession) -> list[Task]:
    list_tasks = await session.execute(select(Task).order_by(id))
    return list_tasks.scalars().all()


async def create_task(session: AsyncSession, base: int, exponent: int):
    new_task = model.Task(id, base=base, exponent=exponent, status=0, result=0)
    session.add(new_task)

    current_result = 1
    for i in range(new_task.exponent):
        time.sleep(1)
        new_task.status = ((i / new_task.exponent) * 100)
        current_result = new_task.base * current_result
    new_task.result = current_result
    new_task.status = 100

    await session.flush()

    """
    def get_task(self: Session, task_id: int):
        return self.query(model.Task).filter(model.Task.id == task_id).first()
    """
