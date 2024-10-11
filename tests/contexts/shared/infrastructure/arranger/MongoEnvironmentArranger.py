from typing import List

from motor.motor_asyncio import AsyncIOMotorClient

from tests.contexts.shared.infrastructure.arranger.EnvironmentArranger import EnvironmentArranger


class MongoEnvironmentArranger(EnvironmentArranger):
    def __init__(
            self,
            client: AsyncIOMotorClient,
            database: str,
    ) -> None:
        super().__init__()

        self.__client = client
        self.__database = self.__client.get_database(database)

    async def arrange(self) -> None:
        await self.__clean_database()

    async def __clean_database(self) -> None:
        collections = await self.__collections()

        for collection in collections:
            await (
                self.__database.get_collection(collection).delete_many({})
            )

    async def __collections(self) -> List[str]:
        return await self.__database.list_collection_names()

    def close(self) -> None:
        self.__client.close()
