import os
from pydantic_settings import BaseSettings
from enum import StrEnum


class Environment(StrEnum):
    PRODUCTION = "production"
    DEVELOPMENT = "development"


class Settings(BaseSettings):
    app_env: str = os.getenv("APP_ENV", Environment.DEVELOPMENT)
    debug: bool = app_env == Environment.DEVELOPMENT
    reload: bool = app_env == Environment.DEVELOPMENT
    proxy_header: bool = app_env == Environment.PRODUCTION
    enable_security_headers: bool = app_env == Environment.PRODUCTION
    log_level: str = "DEBUG" if app_env == Environment.DEVELOPMENT else "INFO"

    # TODO: The reverse proxy IP setting needs be scoped down from "*", but
    # there's some issue with my caddy reverse proxy so there needs to be some
    # more testing before I can ensure this is working as expected.
    trusted_ip: str = os.getenv("REVERSE_PROXY_IP", "*")

    # API settings
    cors_allow_origins: list[str] = os.getenv("CORS_ALLOW_ORIGINS", "*").split(",")
    api_v1_prefix: str = os.getenv("API_V1_PREFIX", "/api/v1")



settings = Settings()
