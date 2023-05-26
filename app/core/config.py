from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'app_title'
    app_description: str = 'app_description'
    secret_key: str = 'secret_key'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    locations_amount: int = 0
    ZIP_CODE_LENGTH = 5
    STATE_NAME_LENGTH = 256
    CITY_NAME_LENGTH = 256
    COORDINATES_LENGTH = 10
    CAR_NUMBER_LENGTH = 5
    CAR_NUMBER_RANGE = (1000, 9999)
    WEIGHT_RANGE = (1, 1000)

    class Config:
        env_file = '.env'

    def set_locations_amount(self, amount: int) -> None:
        self.locations_amount = amount

    def get_locations_amount(self) -> int:
        return self.locations_amount


settings = Settings()
