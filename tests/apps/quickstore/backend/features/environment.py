from behave.runner import Context
from fastapi.testclient import TestClient

from src.apps.quickstore.backend.app import quickstore_backend_app


def before_all(context: Context) -> None:
    context.client = TestClient(quickstore_backend_app)
