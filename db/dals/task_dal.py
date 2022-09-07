from typing import List
import asyncio

from sqlalchemy.future import select
from sqlalchemy.orm import Session


from asynchronous_task_python.db.models.task import Task


class TaskDAL():
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def calculate(task: Task):
        current_result = 1
        for i in range(task.exponent):
            await asyncio.sleep(1)
            current_result = task.base * current_result
            task.status = ((i / task.exponent) * 100)
        task.result = current_result

    async def create_task(self, base: int, exponent: int):
        new_task = Task(base=base, exponent=exponent)
        await TaskDAL.calculate(new_task)
        self.db_session.add(new_task)
        self.db_session.flush()

    async def get_all_tasks(self) -> List[Task]:
        q = await self.db_session.execute(select(Task).order_by(Task.id))
        return q.scalars().all()
