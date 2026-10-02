from collections.abc import Generator
from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from synapse.core.config import app_setting


def create_sqlserver_engine() -> Engine:

    connection_string = (
        f"DRIVER={{{app_setting.sqlserver_driver}}};"
        f"SERVER={app_setting.sqlserver_host};"
        f"DATABASE={app_setting.sqlserver_database};"
        f"UID={app_setting.sqlserver_username};"
        f"PWD={app_setting.sqlserver_password};"
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