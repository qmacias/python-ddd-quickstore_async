from src.contexts.quickstore.productreviews.domain.ProductReviewCreated import ProductReviewCreated


class ProductReviewCreatedMother:
    @staticmethod
    def create(
            aggregate_id: str, user_id: str, product_id: str, rating: int,
    ) -> 'ProductReviewCreated':
        return ProductReviewCreated(aggregate_id, user_id, product_id, rating)
