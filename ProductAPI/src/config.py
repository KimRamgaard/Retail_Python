from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Warehouse API"
    enviroment: str = "DEV"
    db_secret: str = "fnAEKI7XTEACBeppidC6yvgaBz8RKwmqcNdXBzLg"

settings = Settings()

