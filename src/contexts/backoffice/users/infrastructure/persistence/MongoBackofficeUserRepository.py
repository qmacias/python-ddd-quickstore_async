from src.contexts.shared.infrastructure.persistence.MongoRepository import MongoRepository

from src.contexts.backoffice.users.domain.BackofficeUser import BackofficeUser
from src.contexts.backoffice.users.domain.BackofficeUserRepository import BackofficeUserRepository


class MongoBackofficeUserRepository(MongoRepository, BackofficeUserRepository):
    __DATABASE_NAME = 'backoffice'
    __COLLECTION_NAME = 'backoffice_users'

    def __init__(
            self,
            mongodb_uri: str,
    ) -> None:
        super().__init__(mongodb_uri)

    def get_database_name(self) -> str:
        return self.__DATABASE_NAME

    def get_collection_name(self) -> str:
        return self.__COLLECTION_NAME

    async def save(self, user: BackofficeUser) -> None:
        await self.persist(user)
