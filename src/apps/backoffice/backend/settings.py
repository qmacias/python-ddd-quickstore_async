from pydantic_settings import BaseSettings, SettingsConfigDict


class BackofficeSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', extra='ignore',
        env_file_encoding='utf-8', case_sensitive=False,
    )

    MONGODB_URI: str
    BACKOFFICE_BACKEND_APP: str
    BACKOFFICE_BACKEND_APP_HOST: str
    BACKOFFICE_BACKEND_APP_PORT: int


settings = BackofficeSettings()
