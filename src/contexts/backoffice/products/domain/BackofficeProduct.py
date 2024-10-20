from typing import Any, Dict, final

from src.contexts.shared.domain.AggregateRoot import AggregateRoot

from src.contexts.backoffice.products.domain.BackofficeProductId import BackofficeProductId
from src.contexts.backoffice.products.domain.BackofficeProductName import BackofficeProductName
from src.contexts.backoffice.products.domain.BackofficeProductPrice import BackofficeProductPrice
from src.contexts.backoffice.products.domain.BackofficeProductCreated import BackofficeProductCreated


@final
class BackofficeProduct(AggregateRoot):
    def __init__(
            self,
            id: BackofficeProductId,
            name: BackofficeProductName,
            price: BackofficeProductPrice,
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
    ) -> 'BackofficeProduct':
        product = cls(
            BackofficeProductId(id),
            BackofficeProductName(name),
            BackofficeProductPrice(price),
        )

        product.record(
            BackofficeProductCreated(
                product.id.value, product.name.value, product.price.value,
            )
        )

        return product

    @classmethod
    def from_primitives(
            cls, plain_data: Any,
    ) -> 'BackofficeProduct':
        return cls(
            BackofficeProductId(plain_data.get('id')),
            BackofficeProductName(plain_data.get('name')),
            BackofficeProductPrice(plain_data.get('price')),
        )

    @property
    def id(self) -> BackofficeProductId:
        return self._id

    @property
    def name(self) -> BackofficeProductName:
        return self._name

    @property
    def price(self) -> BackofficeProductPrice:
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
