from tests.contexts.shared.domain.Uuid4Mother import Uuid4Mother

from src.contexts.quickstore.products.domain.ProductId import ProductId


class ProductIdMother:
    @staticmethod
    def create(
            value: str,
    ) -> 'ProductId':
        return ProductId(value)

    @classmethod
    def random(cls) -> 'ProductId':
        return cls.create(Uuid4Mother.random())
