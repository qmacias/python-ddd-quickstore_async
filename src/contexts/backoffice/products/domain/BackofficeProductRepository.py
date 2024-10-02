from abc import ABC, abstractmethod

from src.contexts.backoffice.products.domain.BackofficeProduct import BackofficeProduct


class BackofficeProductRepository(ABC):
    @abstractmethod
    async def save(self, product: BackofficeProduct) -> None:
        pass
