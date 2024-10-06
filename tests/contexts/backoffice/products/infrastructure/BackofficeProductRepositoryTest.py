from unittest import IsolatedAsyncioTestCase

from src.apps.container import container
from src.contexts.backoffice.products.domain.BackofficeProductRepository import BackofficeProductRepository

from tests.contexts.shared.infrastructure.arranger.EnvironmentArranger import EnvironmentArranger
from tests.contexts.shared.domain.MotherCreator import MotherCreator
from tests.contexts.shared.domain.products.ProductNameProvider import ProductNameProvider
from tests.contexts.backoffice.products.domain.BackofficeProductMother import BackofficeProductMother


class BackofficeProductRepositoryTest(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.__arranger = container.get(EnvironmentArranger)

        await self.__arranger.arrange()

    async def test_should_save_a_backoffice_product(self) -> None:
        MotherCreator.add_provider(ProductNameProvider)

        product = BackofficeProductMother.random()
        repository = container.get(BackofficeProductRepository)

        await repository.save(product)

    async def asyncTearDown(self):
        await self.__arranger.arrange()

        self.__arranger.close()
