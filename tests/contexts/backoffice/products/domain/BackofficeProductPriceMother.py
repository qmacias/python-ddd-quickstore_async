from tests.contexts.shared.domain.RandomIntMother import RandomIntMother

from src.contexts.backoffice.products.domain.BackofficeProductPrice import BackofficeProductPrice


class BackofficeProductPriceMother:
    @staticmethod
    def create(
            value: int,
    ) -> 'BackofficeProductPrice':
        return BackofficeProductPrice(value)

    @classmethod
    def random(cls) -> 'BackofficeProductPrice':
        return cls.create(RandomIntMother.random(min=1_999, max=9_999))

    @classmethod
    def invalid(cls) -> 'BackofficeProductPrice':
        return cls.create(RandomIntMother.random(min=-9_999, max=-1_999))
