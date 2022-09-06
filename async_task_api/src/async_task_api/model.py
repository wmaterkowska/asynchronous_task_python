from sqlalchemy import Column, Integer, REAL

from async_task_api.src.async_task_api.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    base = Column(Integer, nullable=False, default=0)
    exponent = Column(Integer, nullable=False, default=0)
    status = Column(REAL, nullable=True, default=0)
    result = Column(Integer, nullable=True, default=0)


