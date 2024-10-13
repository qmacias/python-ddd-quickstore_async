import uvicorn

from typing import NamedTuple

from settings import settings


class BackofficeConfig(NamedTuple):
    app: str = settings.BACKOFFICE_BACKEND_APP
    host: str = settings.BACKOFFICE_BACKEND_APP_HOST
    port: int = settings.BACKOFFICE_BACKEND_APP_PORT


def run_backoffice_backend() -> None:
    config = BackofficeConfig()

    uvicorn.run(**config._asdict(), reload=True)
