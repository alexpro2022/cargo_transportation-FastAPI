from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'app_title'
    app_description: str = 'app_description'
    secret_key: str = 'secret_key'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    # postgres_password: str
    number_of_locations: int = 0
    ZIP_CODE_LENGTH = 5
    MIN_WEIGHT = 1
    MAX_WEIGHT = 1000
    CAR_NUMBER_LENGTH = 5
    CAR_NUMBER_RANGE = (1000, 9999)

    class Config:
        env_file = '.env'

    def set_number_of_locations(self, number: int) -> None:
        self.number_of_locations = number


settings = Settings()
