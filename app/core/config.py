from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Course Enroll"
    API_V1_PREFIX: str = "/api/v1"
    ENVIROMENT: str = ""

    DATABASE_URL_ASYNC: str = ""
    DATABASE_URL: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # Ignore undefined env vars
    )


settings = Settings()
