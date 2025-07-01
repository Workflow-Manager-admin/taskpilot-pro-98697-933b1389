from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    app_name: str = "TaskPilot Backend"
    database_url: str = Field(..., env="TASKPILOT_DATABASE_URL")
    jwt_secret_key: str = Field(..., env="JWT_SECRET_KEY")
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 60

    class Config:
        env_file = ".env"


# PUBLIC_INTERFACE
def get_settings() -> Settings:
    """
    Returns app configuration from environment.
    """
    return Settings()
