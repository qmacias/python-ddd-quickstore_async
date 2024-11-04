from typing import TypedDict, Optional

from motor.motor_asyncio import AsyncIOMotorClient

from src.contexts.quickstore.users.domain.UserId import UserId
from src.contexts.shared.infrastructure.persistence.MongoRepository import MongoRepository

from src.contexts.quickstore.users.domain.User import User
from src.contexts.quickstore.users.domain.UserRepository import UserRepository


class UserDocument(TypedDict):
    _id: str
    name: str
    email: str


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

    async def search(self, user_id: UserId) -> Optional[User]:
        document: UserDocument = await self._collection.find_one({'_id': user_id.value})

        return User.from_primitives({'id': document['_id'], 'name': document['name'], 'email': document['email']}) if document else None
