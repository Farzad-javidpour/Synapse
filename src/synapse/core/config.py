from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    sqlserver_host: str
    sqlserver_port: int = 1433
    sqlserver_database: str
    sqlserver_username: str
    sqlserver_password: str
    sqlserver_driver: str = "ODBC Driver 17 for SQL Server"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()