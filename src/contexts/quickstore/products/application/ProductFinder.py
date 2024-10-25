from src.contexts.quickstore.products.domain.Product import Product
from src.contexts.quickstore.products.domain.ProductRepository import ProductRepository
from src.contexts.quickstore.products.domain.ProductFinder import ProductFinder as DomainProductFinder


class ProductFinder:
    def __init__(self, repository: ProductRepository) -> None:
        self.__finder = DomainProductFinder(repository)

    async def __call__(self, id: str) -> Product:
        return await self.__finder(id)
