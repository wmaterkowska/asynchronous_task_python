from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

# DATABASE_URL = "postgresql+asyncpg://localhost:5432/dev"
DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/dev"

engine = create_async_engine(DATABASE_URL, future=True, echo=True)
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession, future=True)
Base = declarative_base()
