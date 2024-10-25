from abc import ABC, abstractmethod
from typing import Optional

from src.contexts.quickstore.users.domain.User import User
from src.contexts.quickstore.users.domain.UserId import UserId


class UserRepository(ABC):
    @abstractmethod
    async def save(self, user: User) -> None:
        pass

    @abstractmethod
    async def search(self, user_id: UserId) -> Optional[User]:
        pass
