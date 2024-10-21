from tests.contexts.shared.domain.RandomIntMother import RandomIntMother

from src.contexts.quickstore.products.domain.ProductPrice import ProductPrice


class ProductPriceMother:
    @staticmethod
    def create(
            value: int,
    ) -> 'ProductPrice':
        return ProductPrice(value)

    @classmethod
    def random(cls) -> 'ProductPrice':
        return cls.create(RandomIntMother.random(min=1_999, max=9_999))
