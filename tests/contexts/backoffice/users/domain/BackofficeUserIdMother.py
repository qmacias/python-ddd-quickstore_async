from tests.contexts.shared.domain.Uuid4Mother import Uuid4Mother

from src.contexts.backoffice.users.domain.BackofficeUserId import BackofficeUserId


class BackofficeUserIdMother:
    @staticmethod
    def create(
            value: str,
    ) -> 'BackofficeUserId':
        return BackofficeUserId(value)

    @classmethod
    def random(cls) -> 'BackofficeUserId':
        return cls.create(Uuid4Mother.random())

    @classmethod
    def invalid(cls) -> 'BackofficeUserId':
        return cls.create(cls.random().value + '.')
