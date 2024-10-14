from typing import Dict

from src.contexts.quickstore.users.domain.User import User
from src.contexts.quickstore.users.domain.UserRepository import UserRepository


class InMemoryUserRepository(UserRepository):
    __users: Dict[str, User] = {}

    async def save(self, user: User) -> None:
        self.__users[user.id.value] = user
