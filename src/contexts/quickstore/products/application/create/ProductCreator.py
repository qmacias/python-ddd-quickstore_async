from src.contexts.quickstore.products.domain.Product import Product
from src.contexts.quickstore.products.domain.ProductRepository import ProductRepository


class ProductCreator:
    def __init__(self, repository: ProductRepository) -> None:
        self.__repository = repository

    async def __call__(self, id: str, name: str, price: int) -> None:
        product = Product.create(id, name, price)

        await self.__repository.save(product)
