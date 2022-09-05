from pydantic import BaseModel


class TaskBase(BaseModel):
    pass


class TaskCreate(TaskBase):
    base: int
    exponent: int


class Task(TaskCreate):
    id: int
    status: float = 0
    result: int = 0

    class Config:
        orm_mode = True
