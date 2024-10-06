from abc import ABC, abstractmethod

from motor.motor_asyncio import AsyncIOMotorClient

from src.contexts.shared.domain.AggregateRoot import AggregateRoot


class MongoRepository(ABC):
    def __init__(
            self,
            mongodb_uri: str,
    ) -> None:
        self.__client = AsyncIOMotorClient(mongodb_uri)
        self.__database = self.__client.get_database(self.get_database_name())
        self.__collection = self.__database.get_collection(self.get_collection_name())

    @abstractmethod
    def get_database_name(self) -> str:
        pass

    @abstractmethod
    def get_collection_name(self) -> str:
        pass

    async def persist(self, entity: AggregateRoot) -> None:
        primitives = entity.to_primitives()

        await self.__collection.update_one(
            {'_id': primitives.pop('id')}, {'$set': primitives}, upsert=True,
        )
