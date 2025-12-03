from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    db_user: str = Field(..., env="DB_USER")
    db_password: str = Field(..., env="DB_PASSWORD")
    db_host: str = Field(..., env="DB_HOST")
    db_port: int = Field(3306, env="DB_PORT")
    db_name: str = Field(..., env="DB_NAME")
    secret_key: str = Field(
        "change-me", env="SECRET_KEY", description="Default is for local development only"
    )
    access_token_expire_minutes: int = Field(60 * 24, env="ACCESS_TOKEN_EXPIRE_MINUTES")


@lru_cache()
def get_settings() -> Settings:
    return Settings()
