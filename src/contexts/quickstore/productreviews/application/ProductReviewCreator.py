from logging import Logger

from src.contexts.shared.domain.EventBus import EventBus

from src.contexts.quickstore.productreviews.domain.ProductReview import ProductReview
from src.contexts.quickstore.productreviews.domain.ProductReviewRepository import ProductReviewRepository


class ProductReviewCreator:
    def __init__(self, repository: ProductReviewRepository, eventbus: EventBus, logger: Logger) -> None:
        self.__repository = repository
        self.__eventbus = eventbus
        self.__logger = logger

    async def __call__(self, id: str, user_id: str, product_id: str, rating: int) -> None:
        productreview = ProductReview.create(id, user_id, product_id, rating)

        await self.__repository.save(productreview)

        events = productreview.pull_domain_events()

        await self.__eventbus.publish(events)

        self.__logger.info(
            'Product Review Created',
            extra={'events': [event.to_primitives() for event in events]}
        )
