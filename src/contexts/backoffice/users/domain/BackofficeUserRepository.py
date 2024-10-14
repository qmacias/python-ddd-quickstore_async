from abc import ABC, abstractmethod
from typing import Sequence

from src.contexts.backoffice.users.domain.BackofficeUser import BackofficeUser


class BackofficeUserRepository(ABC):
    @abstractmethod
    async def save(self, user: BackofficeUser) -> None:
        pass

    @abstractmethod
    async def search_all(self) -> Sequence[BackofficeUser]:
        pass
