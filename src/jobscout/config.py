from typing import Literal

from pydantic import AnyUrl, RedisDsn, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="UTF-8")

    app_env: Literal["dev", "test", "prod"] = "dev"
    log_level: Literal["INFO", "DEBUG", "ERROR", "WARNING"] = "INFO"

    db_host: str = "localhost"
    db_port: int = 5433
    db_name: str
    db_user: str
    db_password: SecretStr

    redis_url: RedisDsn

    mistral_api_key: SecretStr
    mistral_model: str = "mistral-large-latest"

    ollama_base_url: AnyUrl = AnyUrl("http://localhost:11434")
    ollama_model: str = "llama3.2:latest"

    @property
    def postgres_dsn(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_password.get_secret_value()}@{self.db_host}:{self.db_port}/{self.db_name}"
