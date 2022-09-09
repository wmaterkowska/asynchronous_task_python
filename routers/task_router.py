from typing import List
import asyncio

from fastapi import APIRouter, Depends

from db.config import async_session
from db.dals.task_dal import TaskDAL
from db.models.task import Task
from dependencies import get_task_dal
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

loop = asyncio.new_event_loop()


@router.post("/tasks")
async def create_task(base: int, exponent: int, task_dal: TaskDAL = Depends(get_task_dal)):
    async with async_session() as session:
        async with session.begin():
            task_dal = TaskDAL(session)
            T = task_dal.create_task(base, exponent)
            T_R = await task_dal.calculate(T, session)

            return await asyncio.gather(task_dal.update_task(T_R))


@router.get("/tasks")
async def get_all_tasks() -> List[Task]:
    async with async_session() as session:
        async with session.begin():
            task_dal = TaskDAL(session)
            return await asyncio.gather(task_dal.get_all_tasks())
