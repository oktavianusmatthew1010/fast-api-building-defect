from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from sqlalchemy.orm import sessionmaker
from ..config import settings


class Base(DeclarativeBase, MappedAsDataclass):
    pass



#DATABASE_URI = settings.ASYNC_URL
async_engine = create_async_engine(
    settings.ASYNC_URL,  # Use the fully constructed URL
    echo=True,
    pool_size=5,
    max_overflow=10,
    pool_timeout=30,
    pool_pre_ping=True,
    connect_args={
        "ssl": "require" if settings.POSTGRES_SSL else None
    }
)

AsyncSessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
local_session = async_sessionmaker(bind=async_engine, class_=AsyncSessionLocal, expire_on_commit=False)


async def async_get_db() -> AsyncGenerator[AsyncSession, None]:
    async with local_session() as db:
        yield db
