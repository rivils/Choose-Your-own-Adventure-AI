# core/config.py
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    DATABASE_URL: str
    OPENAI_API_KEY: str
    ALLOWED_ORIGINS: List[str]
    API_PREFIX: str = "/api"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()