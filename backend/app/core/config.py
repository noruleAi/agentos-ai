from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    ENVIRONMENT: str

    APP_NAME: str

    DATABASE_URL: str

    REDIS_URL: str

    SECRET_KEY: str

    OPENAI_API_KEY: str

    ALLOWED_ORIGINS: str

    JWT_ALGORITHM: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"

settings = Settings()