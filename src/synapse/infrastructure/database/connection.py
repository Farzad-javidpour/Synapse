from collections.abc import Generator
from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from synapse.core.config import settings


def create_sqlserver_engine() -> Engine:

    connection_string = (
        f"DRIVER={{{settings.sqlserver_driver}}};"
        f"SERVER={settings.sqlserver_host};"
        f"DATABASE={settings.sqlserver_database};"
        f"UID={settings.sqlserver_username};"
        f"PWD={settings.sqlserver_password};"
        "TrustServerCertificate=yes;"
    )
    print("#"* 100)
    print(connection_string)
    connection_url = (
        "mssql+pyodbc:///?odbc_connect="
        + quote_plus(connection_string)
    )

    return create_engine(
        connection_url,
        pool_pre_ping=True,
        pool_size=5,
        max_overflow=10,
    )


engine = create_sqlserver_engine()


SessionLocal = sessionmaker(
    bind=engine,
    class_=Session,
    expire_on_commit=False,
)


def get_db_session() -> Generator[Session, None, None]:
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()