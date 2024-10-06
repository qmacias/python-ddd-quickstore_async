from pydantic_settings import BaseSettings, SettingsConfigDict


class BackofficeSettings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file='.env', extra='ignore',
        env_prefix='BACKOFFICE_', env_file_encoding='utf-8',
    )

    mongodb_uri: str
    backend_app: str
    backend_app_host: str
    backend_app_port: int


backoffice_backend_settings = BackofficeSettings()
