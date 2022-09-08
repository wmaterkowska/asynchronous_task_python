from typing import List
import time
import asyncio

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession


from db.models.task import Task


class TaskDAL():
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_task(self, base: int, exponent: int):
        new_task = Task(base=base, exponent=exponent)

        async with self.db_session:
            current_result = 1
            while new_task.status != 100:
                for i in range(new_task.exponent):
                    time.sleep(1)
                    current_result = new_task.base * current_result
                    new_task.status = ((i / new_task.exponent) * 100)
                    self.db_session.flush()
                new_task.result = current_result
                new_task.status = 100

        self.db_session.add(new_task)
        await self.db_session.flush()

    async def get_all_tasks(self) -> List[Task]:
        q = await self.db_session.execute(select(Task).order_by(Task.id))
        return q.scalars().all()
