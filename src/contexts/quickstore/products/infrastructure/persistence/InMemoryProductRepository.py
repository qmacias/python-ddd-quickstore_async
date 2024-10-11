from typing import Dict, Sequence

from src.contexts.quickstore.products.domain.Product import Product
from src.contexts.quickstore.products.domain.ProductRepository import ProductRepository


class InMemoryProductRepository(ProductRepository):
    __products: Dict[str, Product] = {}

    async def save(self, product: Product) -> None:
        self.__products[product.id.value] = product

    async def search_all(self) -> Sequence[Product]:
        return list(self.__products.values())
