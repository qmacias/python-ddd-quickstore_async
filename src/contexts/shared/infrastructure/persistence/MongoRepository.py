from abc import ABC, abstractmethod

from motor.motor_asyncio import AsyncIOMotorClient

from src.contexts.shared.domain.AggregateRoot import AggregateRoot


class MongoRepository(ABC):
    def __init__(
            self,
            mongodb_uri: str,
    ) -> None:
        self.__client = AsyncIOMotorClient(mongodb_uri)
        self.__database = self.__client.get_database(self.database_name)
        self.__collection = self.__database.get_collection(self.collection_name)

    @property
    @abstractmethod
    def database_name(self) -> str:
        pass

    @property
    @abstractmethod
    def collection_name(self) -> str:
        pass

    async def persist(self, id: str, entity: AggregateRoot) -> None:
        document = entity.to_primitives() | {'_id': id}

        await self.__collection.update_one(
            {'_id': document.pop('id')}, {'$set': document}, upsert=True,
        )
