from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    sqlserver_host: str
    sqlserver_port: int = 1433
    sqlserver_database: str
    sqlserver_username: str
    sqlserver_password: str
    sqlserver_driver: str = "ODBC Driver 17 for SQL Server"

    # -----------------------------
    # API Keys
    # -----------------------------

    google_api_key: str | None = None
    groq_api_key: str | None = None
    openrouter_api_key: str | None = None

    # -----------------------------
    # Ollama
    # -----------------------------

    ollama_base_url: str = "http://localhost:11434"

    # -----------------------------
    # Models
    # -----------------------------

    ollama_model: str = "qwen3:1.7b"
    gemini_model: str = "gemini-2.5-flash"
    groq_model: str = "llama-3.3-70b-versatile"
    openrouter_model: str = "openrouter/free"


    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


app_setting = Settings()