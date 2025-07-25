from logging import Logger

from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock

from src.contexts.backoffice.products.application.BackofficeProductCreator import BackofficeProductCreator
from src.contexts.backoffice.products.domain.BackofficeProductRepository import BackofficeProductRepository
from src.contexts.shared.domain.InvalidArgumentError import InvalidArgumentError
from src.contexts.shared.domain.EventBus import EventBus

from tests.contexts.shared.domain.MotherCreator import MotherCreator
from tests.contexts.shared.domain.products.ProductNameProvider import ProductNameProvider
from tests.contexts.backoffice.products.domain.BackofficeProductMother import BackofficeProductMother
from tests.contexts.backoffice.products.domain.BackofficeProductCreatedMother import BackofficeProductCreatedMother


class BackofficeProductCreatorTest(IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        MotherCreator.add_provider(ProductNameProvider)

        self.__eventbus = AsyncMock(spec=EventBus)
        self.__repository = AsyncMock(spec=BackofficeProductRepository)

        self.__creator = (
            BackofficeProductCreator(self.__repository, self.__eventbus, AsyncMock(spec=Logger))
        )

    async def test_should_create_a_valid_backoffice_product(self) -> None:
        product = BackofficeProductMother.random()

        domain_events = [
            BackofficeProductCreatedMother
            .create(product.id.value, product.name.value, product.price.value),
        ]

        await self.__creator(product.id.value, product.name.value, product.price.value)

        self.__repository.save.assert_called_once_with(product)
        self.__eventbus.publish.assert_called_once_with(domain_events)

    async def test_should_not_create_an_invalid_backoffice_product_with_bad_id(self) -> None:
        with self.assertRaises(InvalidArgumentError):
            product = BackofficeProductMother.with_bad_id()

            await self.__creator(product.id.value, product.name.value, product.price.value)

            self.__repository.save.assert_not_called()
            self.__eventbus.publish.assert_not_called()

    async def test_should_not_create_an_invalid_backoffice_product_with_bad_name(self) -> None:
        with self.assertRaises(InvalidArgumentError):
            product = BackofficeProductMother.with_bad_name()

            await self.__creator(product.id.value, product.name.value, product.price.value)

            self.__repository.save.assert_not_called()
            self.__eventbus.publish.assert_not_called()

    async def test_should_not_create_an_invalid_backoffice_product_with_bad_price(self) -> None:
        with self.assertRaises(InvalidArgumentError):
            product = BackofficeProductMother.with_bad_price()

            await self.__creator(product.id.value, product.name.value, product.price.value)

            self.__repository.save.assert_not_called()
            self.__eventbus.publish.assert_not_called()
