from tests.contexts.shared.domain.MotherCreator import MotherCreator

from src.contexts.quickstore.products.domain.ProductName import ProductName


class ProductNameMother(MotherCreator):
    @staticmethod
    def create(
            value: str,
    ) -> 'ProductName':
        return ProductName(value)

    @classmethod
    def random(cls) -> 'ProductName':
        return cls.create(cls.get_faker().random_product_name())
