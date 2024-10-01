from behave.runner import Context
from fastapi.testclient import TestClient

from src.apps.backoffice.backend.app import backoffice_backend_app


def before_all(context: Context) -> None:
    context.client = TestClient(backoffice_backend_app)
