from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'app_title'
    app_description: str = 'app_description'
    secret_key: str = 'secret_key'
    database_url: str
    # = 'sqlite+aiosqlite:///./fastapi.db'
    # postgres_password: str


settings = Settings()
