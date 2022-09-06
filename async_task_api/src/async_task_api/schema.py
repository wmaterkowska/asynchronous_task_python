from pydantic import BaseModel


class TaskBase(BaseModel):
    pass


class TaskCreate(TaskBase):
    base: int
    exponent: int


class Task(TaskCreate):
    id: int

    status: float
    result: int

    class Config:
        orm_mode = True
