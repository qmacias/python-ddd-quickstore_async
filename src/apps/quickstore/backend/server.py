import uvicorn

from src.apps.quickstore.backend.settings import quickstore_backend_settings


def run_quickstore_backend() -> None:
    uvicorn.run(app=quickstore_backend_settings.quickstore_backend_app,
                host=quickstore_backend_settings.quickstore_backend_app_host,
                port=quickstore_backend_settings.quickstore_backend_app_port, reload=True)
