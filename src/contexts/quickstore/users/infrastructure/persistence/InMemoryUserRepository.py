from typing import Dict, Optional

from src.contexts.quickstore.users.domain.User import User
from src.contexts.quickstore.users.domain.UserId import UserId
from src.contexts.quickstore.users.domain.UserRepository import UserRepository


class InMemoryUserRepository(UserRepository):
    __users: Dict[str, User] = {}

    async def save(self, user: User) -> None:
        self.__users[user.id.value] = user

    async def search(self, user_id: UserId) -> Optional[User]:
        return self.__users.get(user_id.value)
