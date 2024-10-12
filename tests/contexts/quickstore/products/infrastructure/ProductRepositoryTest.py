from typing import Callable, Awaitable
from unittest import IsolatedAsyncioTestCase

from src.apps.container import container

from src.contexts.quickstore.products.domain.ProductRepository import ProductRepository

from tests.contexts.shared.infrastructure.arranger.EnvironmentArranger import EnvironmentArranger
from tests.contexts.shared.domain.MotherCreator import MotherCreator
from tests.contexts.shared.domain.products.ProductNameProvider import ProductNameProvider
from tests.contexts.quickstore.products.domain.ProductMother import ProductMother


class ProductRepositoryTest(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        arranger_provider = container.get(
            Callable[[], Awaitable[EnvironmentArranger]],
        )

        self.__arranger = await arranger_provider()

        await self.__arranger.arrange()

    async def test_should_be_able_to_persist_the_same_product_twice(self) -> None:
        MotherCreator.add_provider(ProductNameProvider)

        product = ProductMother.random()

        repository_provider = container.get(
            Callable[[], Awaitable[ProductRepository]],
        )

        repository = await repository_provider()

        await repository.save(product)
        await repository.save(product)

        persisted_products = await repository.search_all()

        self.assertEqual(len(persisted_products), 1)
        self.assertEqual(persisted_products, [product])

    async def asyncTearDown(self):
        await self.__arranger.arrange()

        self.__arranger.close()
