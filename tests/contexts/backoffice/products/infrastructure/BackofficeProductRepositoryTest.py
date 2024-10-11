from typing import Callable, Awaitable
from unittest import IsolatedAsyncioTestCase

from src.apps.container import container
from src.contexts.backoffice.products.domain.BackofficeProductRepository import BackofficeProductRepository

from tests.contexts.shared.infrastructure.arranger.EnvironmentArranger import EnvironmentArranger
from tests.contexts.shared.domain.MotherCreator import MotherCreator
from tests.contexts.shared.domain.products.ProductNameProvider import ProductNameProvider
from tests.contexts.backoffice.products.domain.BackofficeProductMother import BackofficeProductMother


class BackofficeProductRepositoryTest(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        arranger_provider = container.get(
            Callable[[], Awaitable[EnvironmentArranger]],
        )

        self.__arranger = await arranger_provider()

        await self.__arranger.arrange()

    async def test_should_save_a_backoffice_product(self) -> None:
        MotherCreator.add_provider(ProductNameProvider)

        product = BackofficeProductMother.random()

        repository_provider = container.get(
            Callable[[], Awaitable[BackofficeProductRepository]],
        )

        repository = await repository_provider()

        await repository.save(product)

    async def asyncTearDown(self):
        await self.__arranger.arrange()

        self.__arranger.close()
