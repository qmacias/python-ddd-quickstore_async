from abc import ABC, abstractmethod

from motor.motor_asyncio import AsyncIOMotorClient

from src.contexts.shared.domain.AggregateRoot import AggregateRoot


class MongoRepository(ABC):
    def __init__(
            self, client: AsyncIOMotorClient,
    ) -> None:
        self.__client = client
        self.__database = self.__client.get_database(self.database_name)
        self._collection = self.__database.get_collection(self.collection_name)

    @property
    @abstractmethod
    def database_name(self) -> str:
        pass

    @property
    @abstractmethod
    def collection_name(self) -> str:
        pass

    @property
    def collection(self):
        return self._collection

    async def persist(self, id: str, entity: AggregateRoot) -> None:
        document = entity.to_primitives() | {'_id': id}

        await self._collection.update_one(
            {'_id': document.pop('id')}, {'$set': document}, upsert=True,
        )
