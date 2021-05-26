from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Customer API"
    enviroment: str = "DEV"
    db_secret: str = "fnAEKI7mfjACBW5CyjYVCCs_pnO1XRkc3xxOrUyT"

settings = Settings()

