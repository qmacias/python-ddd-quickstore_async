from typing import Dict, Sequence, Optional

from src.contexts.quickstore.products.domain.Product import Product
from src.contexts.quickstore.products.domain.ProductId import ProductId
from src.contexts.quickstore.products.domain.ProductRepository import ProductRepository


class InMemoryProductRepository(ProductRepository):
    __products: Dict[str, Product] = {}

    async def save(self, product: Product) -> None:
        self.__products[product.id.value] = product

    async def search(self, product_id: ProductId) -> Optional[Product]:
        return self.__products.get(product_id.value)

    async def search_all(self) -> Sequence[Product]:
        return list(self.__products.values())
