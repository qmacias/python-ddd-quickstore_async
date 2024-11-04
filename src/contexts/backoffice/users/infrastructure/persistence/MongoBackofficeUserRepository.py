from typing import TypedDict, Sequence, List

from motor.motor_asyncio import AsyncIOMotorClient

from src.contexts.shared.infrastructure.persistence.MongoRepository import MongoRepository

from src.contexts.backoffice.users.domain.BackofficeUser import BackofficeUser
from src.contexts.backoffice.users.domain.BackofficeUserRepository import BackofficeUserRepository


class UserDocument(TypedDict):
    _id: str
    name: str
    email: str


class MongoBackofficeUserRepository(MongoRepository, BackofficeUserRepository):
    __DATABASE_NAME = 'quickstore-backend-dev'
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

    async def search_all(self) -> Sequence[BackofficeUser]:
        documents: List[UserDocument] = await self._collection.find({}).to_list(None)

        return [BackofficeUser.from_primitives({'id': document['_id'], 'name': document['name'], 'email': document['email']}) for document in documents]
