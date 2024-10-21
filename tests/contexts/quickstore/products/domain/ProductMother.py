from src.contexts.quickstore.products.domain.Product import Product

from tests.contexts.quickstore.products.domain.ProductIdMother import ProductIdMother
from tests.contexts.quickstore.products.domain.ProductNameMother import ProductNameMother
from tests.contexts.quickstore.products.domain.ProductPriceMother import ProductPriceMother


class ProductMother:
    @staticmethod
    def create(
            id: str,
            name: str,
            price: int,
    ) -> 'Product':
        return Product.create(
            ProductIdMother.create(id).value,
            ProductNameMother.create(name).value,
            ProductPriceMother.create(price).value,
        )

    @classmethod
    def random(cls) -> 'Product':
        return cls.create(
            ProductIdMother.random().value,
            ProductNameMother.random().value,
            ProductPriceMother.random().value,
        )
