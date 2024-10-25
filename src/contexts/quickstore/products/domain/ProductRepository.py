from abc import ABC, abstractmethod
from typing import Sequence, Optional

from src.contexts.quickstore.products.domain.Product import Product
from src.contexts.quickstore.products.domain.ProductId import ProductId


class ProductRepository(ABC):
    @abstractmethod
    async def save(self, product: Product) -> None:
        pass

    @abstractmethod
    async def search(self, product_id: ProductId) -> Optional[Product]:
        pass

    @abstractmethod
    async def search_all(self) -> Sequence[Product]:
        pass
