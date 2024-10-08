from unittest import TestCase
from unittest.mock import AsyncMock

from tests.contexts.shared.infrastructure.async_test import async_test
from tests.contexts.shared.domain.MotherCreator import MotherCreator
from tests.contexts.shared.domain.products.ProductNameProvider import ProductNameProvider
from tests.contexts.quickstore.products.domain.ProductMother import ProductMother

from src.contexts.quickstore.products.domain.ProductRepository import ProductRepository
from src.contexts.quickstore.products.application.create.ProductCreator import ProductCreator


class ProductCreatorTest(TestCase):
    @async_test
    async def test_creates_a_product(self) -> None:
        MotherCreator.add_provider(ProductNameProvider)

        product = ProductMother.random()

        repository = AsyncMock(spec=ProductRepository)
        application_service = ProductCreator(repository)

        await application_service(str(product.id), str(product.name))

        repository.save.assert_called_once_with(product)
