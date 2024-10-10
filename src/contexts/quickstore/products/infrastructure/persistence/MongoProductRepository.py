from motor.motor_asyncio import AsyncIOMotorClient

from src.contexts.shared.infrastructure.persistence.MongoRepository import MongoRepository

from src.contexts.quickstore.products.domain.Product import Product
from src.contexts.quickstore.products.domain.ProductRepository import ProductRepository


class MongoProductRepository(MongoRepository, ProductRepository):
    __DATABASE_NAME = 'quickstore'
    __COLLECTION_NAME = 'products'

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

    async def save(self, product: Product) -> None:
        await self.persist(product.id.value, product)
