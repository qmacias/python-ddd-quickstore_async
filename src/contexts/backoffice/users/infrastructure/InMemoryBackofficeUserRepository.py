from typing import Dict

from src.contexts.backoffice.users.domain.BackofficeUser import BackofficeUser
from src.contexts.backoffice.users.domain.BackofficeUserRepository import BackofficeUserRepository


class InMemoryBackofficeUserRepository(BackofficeUserRepository):
    __users: Dict[str, BackofficeUser] = {}

    async def save(self, user: BackofficeUser) -> None:
        self.__users[user.id.value] = user
