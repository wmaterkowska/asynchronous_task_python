from sqlalchemy import Column, Integer, REAL

from async_task_api.src.async_task_api.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    base = Column(Integer)
    exponent = Column(Integer)
    status = Column(REAL)
    result = Column(Integer)


