from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # App
    ENVIRONMENT: str = "development"
    APP_NAME: str = "AgentOS AI"
    
    # Database
    DATABASE_URL: str = "postgresql://postgres:password@localhost/agentos"
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # Security
    SECRET_KEY: str = "your-super-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_HOURS: int = 24
    
    # CORS
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
    ]
    
    # AI Models
    OPENAI_API_KEY: str = ""
    
    class Config:
        env_file = ".env"

settings = Settings()