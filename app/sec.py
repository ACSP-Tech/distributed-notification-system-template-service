# app/config.py
from decouple import config
from pydantic_settings import BaseSettings
from .utils.database import normalize_url

normalized_db = normalize_url(config('DATABASE_URL'))

class Settings(BaseSettings):
    # From your task description
    DATABASE_URL = normalized_db
    REDIS_HOST = config('REDIS_HOST')
    REDIS_PORT = config('REDIS_PORT', default=6379, cast=int)
    REDIS_PASSWORD = config('REDIS_PASSWORD', default=None)

settings = Settings()