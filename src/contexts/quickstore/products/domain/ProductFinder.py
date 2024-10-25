from src.contexts.quickstore.products.domain.Product import Product
from src.contexts.quickstore.products.domain.ProductId import ProductId
from src.contexts.quickstore.products.domain.ProductRepository import ProductRepository
from src.contexts.quickstore.products.domain.ProductDoesNotExists import ProductDoesNotExists


class ProductFinder:
    def __init__(self, repository: ProductRepository) -> None:
        self.__repository = repository

    async def __call__(self, id: str) -> Product:
        product_id = ProductId(id)

        product = await self.__repository.search(product_id)

        if not product:
            raise ProductDoesNotExists(product_id)

        return product
