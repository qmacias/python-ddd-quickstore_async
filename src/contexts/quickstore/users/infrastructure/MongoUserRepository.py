from motor.motor_asyncio import AsyncIOMotorClient

from src.contexts.shared.infrastructure.persistence.MongoRepository import MongoRepository

from src.contexts.quickstore.users.domain.User import User
from src.contexts.quickstore.users.domain.UserRepository import UserRepository


class MongoUserRepository(MongoRepository, UserRepository):
    __DATABASE_NAME = 'quickstore-backend-dev'
    __COLLECTION_NAME = 'users'

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

    async def save(self, user: User) -> None:
        await self.persist(user.id.value, user)
