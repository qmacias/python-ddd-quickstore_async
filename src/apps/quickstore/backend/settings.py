from pydantic_settings import BaseSettings, SettingsConfigDict


class QuickstoreSettings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file='.env', extra='ignore',
        env_prefix='QUICKSTORE_', env_file_encoding='utf-8',
    )

    backend_app: str
    backend_app_host: str
    backend_app_port: int


quickstore_backend_settings = QuickstoreSettings()
