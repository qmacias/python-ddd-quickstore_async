import uvicorn

from src.apps.quickstore.backend.settings import settings


def run_quickstore_backend() -> None:
    uvicorn.run(app=settings.QUICKSTORE_BACKEND_APP,
                host=settings.QUICKSTORE_BACKEND_APP_HOST,
                port=settings.QUICKSTORE_BACKEND_APP_PORT, reload=True)
