from typing import Any, Dict, final

from src.contexts.shared.domain.AggregateRoot import AggregateRoot

from src.contexts.quickstore.products.domain.ProductId import ProductId
from src.contexts.quickstore.products.domain.ProductName import ProductName


@final
class Product(AggregateRoot):
    def __init__(
            self,
            id: ProductId,
            name: ProductName,
    ) -> None:
        super().__init__()

        self._id = id
        self._name = name

    @classmethod
    def create(
            cls,
            id: str,
            name: str,
    ) -> 'Product':
        product = cls(
            ProductId(id),
            ProductName(name),
        )

        return product

    @classmethod
    def from_primitives(
            cls, plain_data: Any,
    ) -> 'Product':
        return cls(
            ProductId(plain_data.get('id')),
            ProductName(plain_data.get('name')),
        )

    @property
    def id(self) -> ProductId:
        return self._id

    @property
    def name(self) -> ProductName:
        return self._name

    @name.setter
    def name(self, name: ProductName) -> None:
        self._name = name  # <-- For duplicator only!

    def to_primitives(self) -> Dict[str, Any]:
        return {
            'id': self._id.value,
            'name': self._name.value,
        }

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self._id == other.id
        return False

    def __repr__(self) -> str:
        attrs: dict = {
            'id': self._id,
            'name': self._name,
        }

        attrs_str: str = ', '.join(
            f'{k}={v!r}' for k, v in attrs.items()
        )

        return f'<{self.__class__.__name__}: {attrs_str}>'
