from abc import ABC, abstractmethod
from typing import Sequence

from src.contexts.quickstore.products.domain.Product import Product


class ProductRepository(ABC):
    @abstractmethod
    async def save(self, product: Product) -> None:
        pass

    @abstractmethod
    async def search_all(self) -> Sequence[Product]:
        pass
