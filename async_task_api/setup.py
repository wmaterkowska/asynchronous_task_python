#!/bin/python3

from sqlalchemy import create_engine, Column, Integer, REAL
from sqlalchemy.orm import declarative_base

from async_task_api.src.async_task_api.model import Task


def main():

    engine = create_engine('sqlite:///:memory:', echo=True)
    base_db = declarative_base()

    class Task(base_db):
        __tablename__ = 'tasks'

        id = Column(Integer, primary_key=True)
        base = Column(Integer)
        exponent = Column(Integer)
        status = Column(REAL)
        result = Column(Integer)


if __name__ == "__main__":
    # Run main program
    main()
