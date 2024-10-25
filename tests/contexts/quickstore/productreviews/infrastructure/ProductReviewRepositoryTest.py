from typing import Callable, Awaitable
from unittest import IsolatedAsyncioTestCase

from src.apps.container import container

from src.contexts.quickstore.productreviews.domain.ProductReviewRepository import ProductReviewRepository

from tests.contexts.shared.infrastructure.arranger.EnvironmentArranger import EnvironmentArranger
from tests.contexts.quickstore.productreviews.domain.ProductReviewMother import ProductReviewMother


class ProductReviewRepositoryTest(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        arranger_provider = container.get(
            Callable[[], Awaitable[EnvironmentArranger]],
        )

        self.__arranger = await arranger_provider()

        await self.__arranger.arrange()

    async def test_should_save_a_productreview(self) -> None:
        productreview = ProductReviewMother.random()

        repository_provider = container.get(
            Callable[[], Awaitable[ProductReviewRepository]],
        )

        repository = await repository_provider()

        await repository.save(productreview)

    async def asyncTearDown(self):
        await self.__arranger.arrange()

        self.__arranger.close()
