from tests.contexts.shared.domain.Uuid4Mother import Uuid4Mother

from src.contexts.quickstore.productreviews.domain.ProductReviewId import ProductReviewId


class ProductReviewIdMother:
    @staticmethod
    def create(
            value: str,
    ) -> 'ProductReviewId':
        return ProductReviewId(value)

    @classmethod
    def random(cls) -> 'ProductReviewId':
        return cls.create(Uuid4Mother.random())

    @classmethod
    def invalid(cls) -> 'ProductReviewId':
        return cls.create(cls.random().value + '.')
