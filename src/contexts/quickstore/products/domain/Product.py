from typing import Any, Dict, final

from src.contexts.shared.domain.AggregateRoot import AggregateRoot

from src.contexts.quickstore.products.domain.ProductId import ProductId
from src.contexts.quickstore.products.domain.ProductName import ProductName
from src.contexts.quickstore.products.domain.ProductPrice import ProductPrice


@final
class Product(AggregateRoot):
    def __init__(
            self,
            id: ProductId,
            name: ProductName,
            price: ProductPrice,
    ) -> None:
        super().__init__()

        self._id = id
        self._name = name
        self._price = price

    @classmethod
    def create(
            cls,
            id: str,
            name: str,
            price: int,
    ) -> 'Product':
        product = cls(
            ProductId(id),
            ProductName(name),
            ProductPrice(price),
        )

        return product

    @classmethod
    def from_primitives(
            cls, plain_data: Any,
    ) -> 'Product':
        return cls(
            ProductId(plain_data.get('id')),
            ProductName(plain_data.get('name')),
            ProductPrice(plain_data.get('price')),
        )

    @property
    def id(self) -> ProductId:
        return self._id

    @property
    def name(self) -> ProductName:
        return self._name

    @property
    def price(self) -> ProductPrice:
        return self._price

    def to_primitives(self) -> Dict[str, Any]:
        return {
            'id': self._id.value,
            'name': self._name.value,
            'price': self._price.value,
        }

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self._id == other.id
        return False

    def __repr__(self) -> str:
        attrs: dict = {
            'id': self._id,
            'name': self._name,
            'price': self._price,
        }

        attrs_str: str = ', '.join(
            f'{k}={v!r}' for k, v in attrs.items()
        )

        return f'<{self.__class__.__name__}: {attrs_str}>'
