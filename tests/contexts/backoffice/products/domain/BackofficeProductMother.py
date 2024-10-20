from src.contexts.backoffice.products.domain.BackofficeProduct import BackofficeProduct

from tests.contexts.backoffice.products.domain.BackofficeProductIdMother import BackofficeProductIdMother
from tests.contexts.backoffice.products.domain.BackofficeProductNameMother import BackofficeProductNameMother
from tests.contexts.backoffice.products.domain.BackofficeProductPriceMother import BackofficeProductPriceMother


class BackofficeProductMother:
    @staticmethod
    def create(
            id: str,
            name: str,
            price: int,
    ) -> 'BackofficeProduct':
        return BackofficeProduct.create(
            BackofficeProductIdMother.create(id).value,
            BackofficeProductNameMother.create(name).value,
            BackofficeProductPriceMother.create(price).value,
        )

    @classmethod
    def random(cls) -> 'BackofficeProduct':
        return cls.create(
            BackofficeProductIdMother.random().value,
            BackofficeProductNameMother.random().value,
            BackofficeProductPriceMother.random().value,
        )

    @staticmethod
    def create_without_events(
            id: str,
            name: str,
            price: int,
    ) -> 'BackofficeProduct':
        return BackofficeProduct(
            BackofficeProductIdMother.create(id),
            BackofficeProductNameMother.create(name),
            BackofficeProductPriceMother.create(price),
        )

    @staticmethod
    def random_without_events() -> 'BackofficeProduct':
        return BackofficeProduct(
            BackofficeProductIdMother.random(),
            BackofficeProductNameMother.random(),
            BackofficeProductPriceMother.random(),
        )

    @classmethod
    def with_bad_id(cls) -> 'BackofficeProduct':
        return cls.create(
            BackofficeProductIdMother.invalid().value,
            BackofficeProductNameMother.random().value,
            BackofficeProductPriceMother.random().value,
        )

    @classmethod
    def with_bad_name(cls) -> 'BackofficeProduct':
        return cls.create(
            BackofficeProductIdMother.random().value,
            BackofficeProductNameMother.invalid().value,
            BackofficeProductPriceMother.random().value,
        )

    @classmethod
    def with_bad_price(cls) -> 'BackofficeProduct':
        return cls.create(
            BackofficeProductIdMother.random().value,
            BackofficeProductNameMother.random().value,
            BackofficeProductPriceMother.invalid().value,
        )
