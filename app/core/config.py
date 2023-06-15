from pydantic import BaseSettings


class Settings(BaseSettings):
    # constants
    DEFAULT_STR = 'To be implemented in .env file'
    DEFAULT_DB_URL = 'sqlite+aiosqlite:///./fastapi.db'
    # environment variables
    app_title: str = DEFAULT_STR
    app_description: str = DEFAULT_STR
    secret_key: str = DEFAULT_STR
    database_url: str = DEFAULT_DB_URL
    SCHEDULER_INTERVAL = 20
    SCHEDULER_TRIGGER = 'interval'
    locations_amount: int = 0
    ZIP_CODE_LENGTH = 5
    STATE_NAME_LENGTH = 256
    CITY_NAME_LENGTH = 256
    COORDINATES_LENGTH = 10
    CAR_NUMBER_LENGTH = 5
    CAR_NUMBER_RANGE = (1000, 9999)
    WEIGHT_RANGE = (1, 1000)
    MAX_RADIUS = 450
    CURRENT_LOCATION = 'current_location'
    CURRENT_ZIP = 'current_zip'
    DELIVERY_LOCATION = 'delivery_location'
    DELIVERY_ZIP = 'delivery_zip'
    ZIP = 'zip'

    class Config:
        env_file = '.env'

    def set_locations_amount(self, amount: int) -> None:
        self.locations_amount = amount

    def get_locations_amount(self) -> int:
        return self.locations_amount


settings = Settings()
