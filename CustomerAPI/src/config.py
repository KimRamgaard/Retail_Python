from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Customer API"
    enviroment: str = "DEV"
    db_secret: str = "fnAEKIZiTfACBbn75dpKStInSsEyERhNwYYt_-Ty"

settings = Settings()

