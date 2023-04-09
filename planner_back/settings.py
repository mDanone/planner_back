from pydantic import BaseSettings


class Settings(BaseSettings):
    postgres_dsn: str

    class Config:
        env_file = "local.env"
