from src.contexts.shared.infrastructure.persistence.MongoRepository import MongoRepository

from src.contexts.backoffice.products.domain.BackofficeProduct import BackofficeProduct
from src.contexts.backoffice.products.domain.BackofficeProductRepository import BackofficeProductRepository


class MongoBackofficeProductRepository(MongoRepository, BackofficeProductRepository):
    __DATABASE_NAME = 'backoffice'
    __COLLECTION_NAME = 'backoffice_products'

    def __init__(
            self,
            mongodb_uri: str,
    ) -> None:
        super().__init__(mongodb_uri)

    def get_database_name(self) -> str:
        return self.__DATABASE_NAME

    def get_collection_name(self) -> str:
        return self.__COLLECTION_NAME

    async def save(self, product: BackofficeProduct) -> None:
        await self.persist(product)
