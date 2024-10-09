import uvicorn

from settings import settings


def run_backoffice_backend() -> None:
    uvicorn.run(app=settings.BACKOFFICE_BACKEND_APP,
                host=settings.BACKOFFICE_BACKEND_APP_HOST,
                port=settings.BACKOFFICE_BACKEND_APP_PORT, reload=True)
