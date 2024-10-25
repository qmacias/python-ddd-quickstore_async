from datetime import datetime
from typing import Any, Dict, Optional, final

from src.contexts.shared.domain.DomainEvent import DomainEvent


@final
class ProductReviewCreated(DomainEvent):
    EVENT_TYPE = 'productreview.created'

    def __init__(
            self,
            aggregate_id: str,
            user_id: str,
            product_id: str,
            rating: int,
            event_id: Optional[str] = None,
            occurred_on: Optional[datetime] = None,
    ) -> None:
        super().__init__(self.EVENT_TYPE, aggregate_id, event_id, occurred_on)

        self._user_id = user_id
        self._product_id = product_id
        self._rating = rating

    @property
    def user_id(self) -> str:
        return self._user_id

    @property
    def product_id(self) -> str:
        return self._product_id

    @property
    def rating(self) -> int:
        return self._rating

    def to_primitives(self) -> Dict[Any, Any]:
        return {
            'data': {
                'eventId': self._event_id,
                'type': self.EVENT_TYPE,
                'occurred_on': str(self._occurred_on),
                'aggregateId': self._aggregate_id,
                'attributes': {
                    'userId': self._user_id,
                    'productId': self._product_id,
                    'rating': self._rating,
                },
            },
            'meta': {
                'attempts': 0,
            }
        }
