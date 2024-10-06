from motor.motor_asyncio import AsyncIOMotorClient

from src.contexts.backoffice.products.domain.BackofficeProduct import BackofficeProduct
from src.contexts.backoffice.products.domain.BackofficeProductRepository import BackofficeProductRepository


class MongoBackofficeProductRepository(BackofficeProductRepository):
    __DATABASE_NAME = 'backoffice'
    __COLLECTION_NAME = 'backoffice_products'

    def __init__(
            self,
            mongodb_uri: str,
    ) -> None:
        self.__client = AsyncIOMotorClient(mongodb_uri)
        self.__database = self.__client.get_database(self.__DATABASE_NAME)
        self.__collection = self.__database.get_collection(self.__COLLECTION_NAME)

    async def save(self, product: BackofficeProduct) -> None:
        document = product.to_primitives()

        await self.__collection.update_one(
            {'_id': document.pop('id')}, {'$set': document}, upsert=True,
        )
