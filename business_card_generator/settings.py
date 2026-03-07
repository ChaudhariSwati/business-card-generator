from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_environment: str = "production"
    force_https: bool = False  # Disabled for serverless/proxy environments like Vercel
