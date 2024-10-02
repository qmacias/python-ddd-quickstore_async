from tests.contexts.shared.domain.MotherCreator import MotherCreator

from src.contexts.backoffice.products.domain.BackofficeProductName import BackofficeProductName


class BackofficeProductNameMother(MotherCreator):
    @staticmethod
    def create(
            value: str,
    ) -> 'BackofficeProductName':
        return BackofficeProductName(value)

    @classmethod
    def random(cls) -> 'BackofficeProductName':
        return cls.create(cls.get_faker().random_product_name())

    @classmethod
    def invalid(cls) -> 'BackofficeProductName':
        return cls.create(cls.get_faker().invalid_product_name())
