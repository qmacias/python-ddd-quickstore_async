from motor.motor_asyncio import AsyncIOMotorClient

from src.contexts.shared.infrastructure.persistence.MongoRepository import MongoRepository

from src.contexts.backoffice.users.domain.BackofficeUser import BackofficeUser
from src.contexts.backoffice.users.domain.BackofficeUserRepository import BackofficeUserRepository


class MongoBackofficeUserRepository(MongoRepository, BackofficeUserRepository):
    __DATABASE_NAME = 'backoffice'
    __COLLECTION_NAME = 'backoffice_users'

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

    async def save(self, user: BackofficeUser) -> None:
        await self.persist(user.id.value, user)
