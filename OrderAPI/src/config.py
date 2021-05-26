from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Order API"
    enviroment: str = "DEV"
    db_secret: str = "fnAEKI7OuaACBZHL0esMnuLVhJ9WgWlzpo8q9w8g"


settings = Settings()
