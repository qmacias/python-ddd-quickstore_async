from src.contexts.quickstore.productreviews.domain.ProductReview import ProductReview

from tests.contexts.quickstore.users.domain.UserIdMother import UserIdMother
from tests.contexts.quickstore.products.domain.ProductIdMother import ProductIdMother

from tests.contexts.quickstore.productreviews.domain.ProductReviewIdMother import ProductReviewIdMother
from tests.contexts.quickstore.productreviews.domain.ProductReviewRatingMother import ProductReviewRatingMother


class ProductReviewMother:
    @staticmethod
    def create(
            id: str,
            user_id: str,
            product_id: str,
            rating: int,
    ) -> 'ProductReview':
        return ProductReview.create(
            ProductReviewIdMother.create(id).value,
            UserIdMother.create(user_id).value,
            ProductIdMother.create(product_id).value,
            ProductReviewRatingMother.create(rating).value,
        )

    @classmethod
    def random(cls) -> 'ProductReview':
        return cls.create(
            ProductReviewIdMother.random().value,
            UserIdMother.random().value,
            ProductIdMother.random().value,
            ProductReviewRatingMother.random().value,
        )

    @staticmethod
    def create_without_events(
            id: str,
            user_id: str,
            product_id: str,
            rating: int,
    ) -> 'ProductReview':
        return ProductReview(
            ProductReviewIdMother.create(id),
            UserIdMother.create(user_id),
            ProductIdMother.create(product_id),
            ProductReviewRatingMother.create(rating),
        )

    @staticmethod
    def random_without_events() -> 'ProductReview':
        return ProductReview(
            ProductReviewIdMother.random(),
            UserIdMother.random(),
            ProductIdMother.random(),
            ProductReviewRatingMother.random(),
        )

    @classmethod
    def with_bad_id(cls) -> 'ProductReview':
        return cls.create(
            ProductReviewIdMother.invalid().value,
            UserIdMother.random().value,
            ProductIdMother.random().value,
            ProductReviewRatingMother.random().value,
        )

    @classmethod
    def with_bad_rating(cls) -> 'ProductReview':
        return cls.create(
            ProductReviewIdMother.random().value,
            ProductReviewRatingMother.invalid().value,
        )
