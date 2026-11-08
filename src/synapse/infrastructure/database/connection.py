from collections.abc import AsyncGenerator
from urllib.parse import quote_plus

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from synapse.core.config import app_setting

class Base(DeclarativeBase):
    pass

def create_sqlserver_engine():
    connection_string = (
        f"DRIVER={{{app_setting.sqlserver_driver}}};"
        f"SERVER={app_setting.sqlserver_host};"
        f"DATABASE={app_setting.sqlserver_database};"
        f"UID={app_setting.sqlserver_username};"
        f"PWD={app_setting.sqlserver_password};"
        "TrustServerCertificate=yes;"
    )
    connection_url = (
        "mssql+aioodbc:///?odbc_connect="
        + quote_plus(connection_string)
    )

    return create_async_engine(
        connection_url,
        pool_pre_ping=True,
        pool_size=5,
        max_overflow=10,
    )


engine = create_sqlserver_engine()


AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session