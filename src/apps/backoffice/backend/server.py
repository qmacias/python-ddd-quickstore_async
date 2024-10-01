import uvicorn

from src.apps.backoffice.backend.settings import backoffice_backend_settings


def run_backoffice_backend() -> None:
    uvicorn.run(app=backoffice_backend_settings.backoffice_backend_app,
                host=backoffice_backend_settings.backoffice_backend_app_host,
                port=backoffice_backend_settings.backoffice_backend_app_port, reload=True)
