from abc import ABC, abstractmethod

from src.contexts.quickstore.users.domain.User import User


class UserRepository(ABC):
    @abstractmethod
    async def save(self, user: User) -> None:
        pass
