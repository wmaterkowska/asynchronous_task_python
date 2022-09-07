from db.config import async_session
from db.dals.task_dal import TaskDAL


async def get_task_dal():
    async with async_session() as session:
        async with session.begin():
            yield TaskDAL(session)
