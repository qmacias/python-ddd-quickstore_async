from typing import Dict, Any, final

from src.contexts.shared.domain.AggregateRoot import AggregateRoot

from src.contexts.quickstore.users.domain.UserId import UserId
from src.contexts.quickstore.products.domain.ProductId import ProductId

from src.contexts.quickstore.productreviews.domain.ProductReviewId import ProductReviewId
from src.contexts.quickstore.productreviews.domain.ProductReviewRating import ProductReviewRating
from src.contexts.quickstore.productreviews.domain.ProductReviewCreated import ProductReviewCreated


@final
class ProductReview(AggregateRoot):
    def __init__(
            self,
            id: ProductReviewId,
            user_id: UserId,
            product_id: ProductId,
            rating: ProductReviewRating,
    ) -> None:
        super().__init__()

        self._id = id
        self._user_id = user_id
        self._product_id = product_id
        self._rating = rating

    @classmethod
    def create(
            cls,
            id: str,
            user_id: str,
            product_id: str,
            rating: int,
    ) -> 'ProductReview':
        productreview = cls(
            ProductReviewId(id),
            UserId(user_id),
            ProductId(product_id),
            ProductReviewRating(rating),
        )

        productreview.record(
            ProductReviewCreated(
                productreview.id.value,
                productreview.user_id.value,
                productreview.product_id.value,
                productreview.rating.value,
            )
        )

        return productreview

    @classmethod
    def from_primitives(
            cls, plain_data: Any,
    ) -> 'ProductReview':
        return cls(
            ProductReviewId(plain_data.get('id')),
            UserId(plain_data.get('user_id')),
            ProductId(plain_data.get('product_id')),
            ProductReviewRating(plain_data.get('rating')),
        )

    @property
    def id(self) -> ProductReviewId:
        return self._id

    @property
    def user_id(self) -> UserId:
        return self._user_id

    @property
    def product_id(self) -> ProductId:
        return self._product_id

    @property
    def rating(self) -> ProductReviewRating:
        return self._rating

    def to_primitives(self) -> Dict[str, Any]:
        return {
            'id': self._id.value,
            'user_id': self._user_id.value,
            'product_id': self._product_id.value,
            'rating': self._rating.value,
        }

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self._id == other.id
        return False

    def __repr__(self) -> str:
        attrs: dict = {
            'id': self._id,
            'user_id': self._user_id,
            'product_id': self._product_id,
            'rating': self._rating,
        }

        attrs_str: str = ', '.join(
            f'{k}={v!r}' for k, v in attrs.items()
        )

        return f'<{self.__class__.__name__}: {attrs_str}>'
