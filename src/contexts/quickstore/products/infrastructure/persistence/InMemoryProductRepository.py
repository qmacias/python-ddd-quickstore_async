from typing import Dict

from src.contexts.quickstore.products.domain.Product import Product
from src.contexts.quickstore.products.domain.ProductRepository import ProductRepository


class InMemoryProductRepository(ProductRepository):
    __products: Dict[str, Product] = {}

    async def save(self, product: Product) -> None:
        self.__products[product.id.value] = product
