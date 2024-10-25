from logging import Logger

from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock

from src.contexts.quickstore.productreviews.application.ProductReviewCreator import ProductReviewCreator
from src.contexts.quickstore.productreviews.domain.ProductReviewRepository import ProductReviewRepository
from src.contexts.shared.domain.InvalidArgumentError import InvalidArgumentError
from src.contexts.shared.domain.EventBus import EventBus

from tests.contexts.quickstore.productreviews.domain.ProductReviewMother import ProductReviewMother
from tests.contexts.quickstore.productreviews.domain.ProductReviewCreatedMother import ProductReviewCreatedMother


class ProductReviewCreatorTest(IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.__eventbus = AsyncMock(spec=EventBus)
        self.__repository = AsyncMock(spec=ProductReviewRepository)

        self.__creator = (
            ProductReviewCreator(self.__repository, self.__eventbus, AsyncMock(spec=Logger))
        )

    async def test_should_create_a_valid_productreview(self) -> None:
        productreview = ProductReviewMother.random()

        domain_events = [
            ProductReviewCreatedMother.create(
                productreview.id.value,
                productreview.user_id.value,
                productreview.product_id.value,
                productreview.rating.value,
            )
        ]

        await self.__creator(
            productreview.id.value,
            productreview.user_id.value,
            productreview.product_id.value,
            productreview.rating.value,
        )

        self.__repository.save.assert_called_once_with(productreview)
        self.__eventbus.publish.assert_called_once_with(domain_events)

    async def test_should_not_create_an_invalid_productreview_with_bad_id(self) -> None:
        with self.assertRaises(InvalidArgumentError):
            productreview = ProductReviewMother.with_bad_id()

            await self.__creator(
                productreview.id.value,
                productreview.user_id.value,
                productreview.product_id.value,
                productreview.rating.value,
            )

            self.__repository.save.assert_not_called()
            self.__eventbus.publish.assert_not_called()

    async def test_should_not_create_an_invalid_productreview_with_bad_rating(self) -> None:
        with self.assertRaises(InvalidArgumentError):
            productreview = ProductReviewMother.with_bad_rating()

            await self.__creator(
                productreview.id.value,
                productreview.user_id.value,
                productreview.product_id.value,
                productreview.rating.value,
            )

            self.__repository.save.assert_not_called()
            self.__eventbus.publish.assert_not_called()
