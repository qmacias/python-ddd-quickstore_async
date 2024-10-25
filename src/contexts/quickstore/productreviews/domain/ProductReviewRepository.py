from abc import ABC, abstractmethod

from src.contexts.quickstore.productreviews.domain.ProductReview import ProductReview


class ProductReviewRepository(ABC):
    @abstractmethod
    async def save(self, productreview: ProductReview) -> None:
        pass
