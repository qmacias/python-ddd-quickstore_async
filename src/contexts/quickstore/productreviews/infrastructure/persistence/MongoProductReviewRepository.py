from motor.motor_asyncio import AsyncIOMotorClient

from src.contexts.shared.infrastructure.persistence.MongoRepository import MongoRepository

from src.contexts.quickstore.productreviews.domain.ProductReview import ProductReview
from src.contexts.quickstore.productreviews.domain.ProductReviewRepository import ProductReviewRepository


class MongoProductReviewRepository(MongoRepository, ProductReviewRepository):
    __DATABASE_NAME = 'quickstore-backend-dev'
    __COLLECTION_NAME = 'product_reviews'

    def __init__(
            self, client: AsyncIOMotorClient,
    ) -> None:
        super().__init__(client)

    @property
    def database_name(self) -> str:
        return self.__DATABASE_NAME

    @property
    def collection_name(self) -> str:
        return self.__COLLECTION_NAME

    async def save(self, productreview: ProductReview) -> None:
        await self.persist(productreview.id.value, productreview)
