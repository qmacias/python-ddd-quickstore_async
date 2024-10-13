import uvicorn

from typing import NamedTuple

from settings import settings


class QuickstoreConfig(NamedTuple):
    app: str = settings.QUICKSTORE_BACKEND_APP
    host: str = settings.QUICKSTORE_BACKEND_APP_HOST
    port: int = settings.QUICKSTORE_BACKEND_APP_PORT


def run_quickstore_backend() -> None:
    config = QuickstoreConfig()

    uvicorn.run(**config._asdict(), reload=True)
