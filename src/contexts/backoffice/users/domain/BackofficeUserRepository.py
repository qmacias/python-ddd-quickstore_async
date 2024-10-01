from abc import ABC, abstractmethod

from src.contexts.backoffice.users.domain.BackofficeUser import BackofficeUser


class BackofficeUserRepository(ABC):
    @abstractmethod
    async def save(self, user: BackofficeUser) -> None:
        pass
