from pydantic_settings import BaseSettings, SettingsConfigDict


class QuickstoreSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', extra='ignore',
        env_prefix='QUICKSTORE_', env_file_encoding='utf-8',
    )

    quickstore_backend_app: str
    quickstore_backend_app_host: str
    quickstore_backend_app_port: int


quickstore_backend_settings = QuickstoreSettings()
