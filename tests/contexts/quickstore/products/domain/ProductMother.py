from src.contexts.quickstore.products.domain.Product import Product

from tests.contexts.quickstore.products.domain.ProductIdMother import ProductIdMother
from tests.contexts.quickstore.products.domain.ProductNameMother import ProductNameMother


class ProductMother:
    @staticmethod
    def create(
            id: str,
            name: str,
    ) -> 'Product':
        return Product.create(
            ProductIdMother.create(id).value,
            ProductNameMother.create(name).value,
        )

    @classmethod
    def random(cls) -> 'Product':
        return cls.create(
            ProductIdMother.random().value,
            ProductNameMother.random().value,
        )
