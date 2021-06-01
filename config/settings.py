from pydantic import BaseSettings


class Settings(BaseSettings):
    amazon_cognito_region: str
    amazon_cognito_user_pool_id: str
    amazon_cognito_client_id: str
    amazon_cognito_client_secret: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
