from sqlalchemy import Column, Integer, REAL

from asynchronous_task_python.db.config import Base


class Task(Base):
    __tablename__ = 'tasks'


    id = Column(Integer, primary_key=True)
    base = Column(Integer, nullable=False)
    exponent = Column(Integer, nullable=False)
    status = Column(REAL, nullable=True)
    result = Column(Integer, nullable=True)
