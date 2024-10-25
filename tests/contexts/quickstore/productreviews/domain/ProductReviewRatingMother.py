from tests.contexts.shared.domain.RandomIntMother import RandomIntMother

from src.contexts.quickstore.productreviews.domain.ProductReviewRating import ProductReviewRating


class ProductReviewRatingMother:
    @staticmethod
    def create(
            value: int,
    ) -> 'ProductReviewRating':
        return ProductReviewRating(value)

    @classmethod
    def random(cls) -> 'ProductReviewRating':
        return cls.create(RandomIntMother.random(min=0, max=5))

    @classmethod
    def invalid(cls) -> 'ProductReviewRating':
        return cls.create(RandomIntMother.random(min=-6, max=-1))
