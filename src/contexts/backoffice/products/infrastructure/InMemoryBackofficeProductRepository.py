from typing import Dict

from src.contexts.backoffice.products.domain.BackofficeProduct import BackofficeProduct
from src.contexts.backoffice.products.domain.BackofficeProductRepository import BackofficeProductRepository


class InMemoryBackofficeProductRepository(BackofficeProductRepository):
    __products: Dict[str, BackofficeProduct] = {}

    async def save(self, product: BackofficeProduct) -> None:
        self.__products[product.id.value] = product
