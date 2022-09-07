from typing import List, Optional
import time

from fastapi import APIRouter, Depends

from db.config import engine, Base, async_session
from db.dals.task_dal import TaskDAL
from db.models.task import Task
from dependencies import get_task_dal

router = APIRouter()


@router.post("/tasks")
async def create_task(base: int, exponent: int, task_dal: TaskDAL = Depends(get_task_dal)):
    async with async_session() as session:
        async with session.begin():
            task_dal = TaskDAL(session)
            return await task_dal.create_task(base, exponent)


@router.get("/tasks")
async def get_all_tasks() -> List[Task]:
    async with async_session() as session:
        async with session.begin():
            task_dal = TaskDAL(session)
            return await task_dal.get_all_tasks()
