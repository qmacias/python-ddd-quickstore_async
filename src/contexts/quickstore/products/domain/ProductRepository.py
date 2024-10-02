from abc import ABC, abstractmethod

from src.contexts.quickstore.products.domain.Product import Product


class ProductRepository(ABC):
    @abstractmethod
    async def save(self, product: Product) -> None:
        pass
