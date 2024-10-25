from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock

from src.contexts.quickstore.products.application.ProductFinder import ProductFinder
from src.contexts.quickstore.products.domain.ProductRepository import ProductRepository
from src.contexts.quickstore.products.domain.ProductDoesNotExists import ProductDoesNotExists

from tests.contexts.shared.domain.MotherCreator import MotherCreator
from tests.contexts.shared.domain.products.ProductNameProvider import ProductNameProvider
from tests.contexts.quickstore.products.domain.ProductMother import ProductMother


class ProductFinderTest(IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        MotherCreator.add_provider(ProductNameProvider)

        self.__repository = AsyncMock(spec=ProductRepository)

        self.__finder = ProductFinder(self.__repository)

    async def test_should_find_an_existing_product(self) -> None:
        existing_product = ProductMother.random()

        self.__repository.search.return_value = existing_product

        expected_product = await self.__finder(existing_product.id.value)

        self.__repository.search.assert_called_once_with(existing_product.id)
        self.assertEqual(existing_product, expected_product)

    async def test_should_raise_an_exception_when_product_does_not_exists(self) -> None:
        product = ProductMother.random()

        self.__repository.search.return_value = None

        with self.assertRaises(ProductDoesNotExists):
            await self.__finder(product.id.value)

            self.__repository.search.assert_called_once_with(product.id)
