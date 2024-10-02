from unittest import TestCase

from src.apps.container import container
from src.contexts.backoffice.products.domain.BackofficeProductRepository import BackofficeProductRepository

from tests.contexts.shared.infrastructure.async_test import async_test
from tests.contexts.shared.domain.MotherCreator import MotherCreator
from tests.contexts.shared.domain.products.ProductNameProvider import ProductNameProvider
from tests.contexts.backoffice.products.domain.BackofficeProductMother import BackofficeProductMother


class BackofficeProductRepositoryTest(TestCase):
    def setUp(self) -> None:
        MotherCreator.add_provider(ProductNameProvider)

        self.__repository = container.get(BackofficeProductRepository)

    @async_test
    async def test_should_save_a_backoffice_product(self) -> None:
        product = BackofficeProductMother.random()

        await self.__repository.save(product)
