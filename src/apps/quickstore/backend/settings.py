from pydantic_settings import BaseSettings, SettingsConfigDict


class QuickstoreSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', extra='ignore',
        env_file_encoding='utf-8', case_sensitive=False,
    )

    MONGODB_URI: str
    QUICKSTORE_BACKEND_APP: str
    QUICKSTORE_BACKEND_APP_HOST: str
    QUICKSTORE_BACKEND_APP_PORT: int


settings = QuickstoreSettings()
