from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from core.config import settings


def create_sqlserver_engine() -> Engine:

    connection_string = (
        f"DRIVER={{{settings.sqlserver_driver}}};"
        f"SERVER={settings.sqlserver_host},{settings.sqlserver_port};"
        f"DATABASE={settings.sqlserver_database};"
        f"UID={settings.sqlserver_username};"
        f"PWD={settings.sqlserver_password};"
        "TrustServerCertificate=yes;"
    )

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