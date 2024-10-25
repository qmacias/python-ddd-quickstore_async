from typing import Dict

from src.contexts.quickstore.productreviews.domain.ProductReview import ProductReview
from src.contexts.quickstore.productreviews.domain.ProductReviewRepository import ProductReviewRepository


class InMemoryProductReviewRepository(ProductReviewRepository):
    __productreviews: Dict[str, ProductReview] = {}

    async def save(self, productreview: ProductReview) -> None:
        self.__productreviews[productreview.id.value] = productreview
