from pydantic_settings import BaseSettings, SettingsConfigDict


class BackofficeSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', extra='ignore',
        env_prefix='BACKOFFICE_', env_file_encoding='utf-8',
    )

    backoffice_backend_app: str
    backoffice_backend_app_host: str
    backoffice_backend_app_port: int


backoffice_backend_settings = BackofficeSettings()
