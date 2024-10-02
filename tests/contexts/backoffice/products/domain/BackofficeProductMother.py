from src.contexts.backoffice.products.domain.BackofficeProduct import BackofficeProduct

from tests.contexts.backoffice.products.domain.BackofficeProductIdMother import BackofficeProductIdMother
from tests.contexts.backoffice.products.domain.BackofficeProductNameMother import BackofficeProductNameMother


class BackofficeProductMother:
    @staticmethod
    def create(
            id: str,
            name: str,
    ) -> 'BackofficeProduct':
        return BackofficeProduct.create(
            BackofficeProductIdMother.create(id).value,
            BackofficeProductNameMother.create(name).value,
        )

    @classmethod
    def random(cls) -> 'BackofficeProduct':
        return cls.create(
            BackofficeProductIdMother.random().value,
            BackofficeProductNameMother.random().value,
        )

    @staticmethod
    def create_without_events(
            id: str,
            name: str,
    ) -> 'BackofficeProduct':
        return BackofficeProduct(
            BackofficeProductIdMother.create(id),
            BackofficeProductNameMother.create(name),
        )

    @staticmethod
    def random_without_events() -> 'BackofficeProduct':
        return BackofficeProduct(
            BackofficeProductIdMother.random(),
            BackofficeProductNameMother.random(),
        )

    @classmethod
    def with_bad_id(cls) -> 'BackofficeProduct':
        return cls.create(
            BackofficeProductIdMother.invalid().value,
            BackofficeProductNameMother.random().value,
        )

    @classmethod
    def with_bad_name(cls) -> 'BackofficeProduct':
        return cls.create(
            BackofficeProductIdMother.random().value,
            BackofficeProductNameMother.invalid().value,
        )
