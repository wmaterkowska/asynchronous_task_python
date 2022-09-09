from turtle import update
from typing import List
import time
import asyncio

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession


from db.models.task import Task


class TaskDAL():
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def calculate(self, task: Task, db_session: AsyncSession):
        current_result = 1
        for i in range(task.exponent):
            await asyncio.sleep(1)
            current_result = task.base * current_result
            task.status = ((i / task.exponent) * 100)
            await db_session.flush()
        task.result = current_result
        task.status = 100

        return await db_session.flush()

    def create_task(self, base: int, exponent: int):
        new_task = Task(base=base, exponent=exponent)

        new_task.status = 0
        new_task.result = 0
        self.db_session.add(new_task)

        return new_task

    async def update_task(self, task: Task):
        self.db_session.flush()

    async def get_all_tasks(self) -> List[Task]:
        q = await self.db_session.execute(select(Task).order_by(Task.id))
        return q.scalars().all()
