from tests.contexts.shared.domain.Uuid4Mother import Uuid4Mother

from src.contexts.backoffice.products.domain.BackofficeProductId import BackofficeProductId


class BackofficeProductIdMother:
    @staticmethod
    def create(
            value: str,
    ) -> 'BackofficeProductId':
        return BackofficeProductId(value)

    @classmethod
    def random(cls) -> 'BackofficeProductId':
        return cls.create(Uuid4Mother.random())

    @classmethod
    def invalid(cls) -> 'BackofficeProductId':
        return cls.create(cls.random().value + '.')
