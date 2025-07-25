from typing import TypedDict, Optional, Sequence, List

from motor.motor_asyncio import AsyncIOMotorClient

from src.contexts.quickstore.products.domain.ProductId import ProductId
from src.contexts.shared.infrastructure.persistence.MongoRepository import MongoRepository

from src.contexts.quickstore.products.domain.Product import Product
from src.contexts.quickstore.products.domain.ProductRepository import ProductRepository


class ProductDocument(TypedDict):
    _id: str
    name: str
    price: int


class MongoProductRepository(MongoRepository, ProductRepository):
    __DATABASE_NAME = 'quickstore-backend-dev'
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

    async def search(self, product_id: ProductId) -> Optional[Product]:
        document: ProductDocument = await self._collection.find_one({'_id': product_id.value})

        return Product.from_primitives({'id': document['_id'], 'name': document['name'], 'price': document['price']}) if document else None

    async def search_all(self) -> Sequence[Product]:
        documents: List[ProductDocument] = await self._collection.find({}).to_list(None)

        return [Product.from_primitives({'id': document['_id'], 'name': document['name'], 'price': document['price']}) for document in documents]
