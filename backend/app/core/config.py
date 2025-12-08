"""Application configuration and settings."""
import os
from typing import Literal
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application settings with environment variable support."""

    # Application
    APP_NAME: str = "DaisyUI Healthcare API"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: Literal["development", "staging", "production"] = Field(
        default="development", alias="ENV"
    )
    DEBUG: bool = Field(default=True)

    # Database
    DATABASE_URL: str = Field(
        default="mysql+pymysql://root:root@localhost:3306/daisyui_db",
        description="Database connection URL"
    )

    # JWT Security
    SECRET_KEY: str = Field(
        default="your-secret-key-change-in-production",
        description="Secret key for JWT encoding/decoding"
    )
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # CORS
    CORS_ORIGINS: list[str] = Field(
        default=["http://localhost:5173", "http://localhost:3000"]
    )
    CORS_CREDENTIALS: bool = True
    CORS_METHODS: list[str] = ["*"]
    CORS_HEADERS: list[str] = ["*"]

    # Redis (optional)
    REDIS_URL: str = Field(
        default="redis://localhost:6379",
        description="Redis connection URL for caching and task queue"
    )
    USE_REDIS: bool = False

    # Logging
    LOG_LEVEL: str = Field(default="INFO")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


# Global settings instance
settings = Settings()
