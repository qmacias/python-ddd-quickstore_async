from behave.runner import Context
from behave.api.async_step import async_run_until_complete

from fastapi.testclient import TestClient

from src.apps.container import container
from src.apps.backoffice.backend.app import backoffice_backend_app

from tests.contexts.shared.infrastructure.arranger.EnvironmentArranger import EnvironmentArranger

arranger = container.get(EnvironmentArranger)


@async_run_until_complete
async def before_all(context: Context) -> None:
    await arranger.arrange()

    context.client = TestClient(backoffice_backend_app)


@async_run_until_complete
async def after_all(context: Context) -> None:
    await arranger.arrange()

    arranger.close()

    context.client.close()
