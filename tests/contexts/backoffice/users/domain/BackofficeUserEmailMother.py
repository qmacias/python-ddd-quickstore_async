from tests.contexts.shared.domain.MotherCreator import MotherCreator

from src.contexts.backoffice.users.domain.BackofficeUserEmail import BackofficeUserEmail


class BackofficeUserEmailMother(MotherCreator):
    @staticmethod
    def create(
            value: str,
    ) -> 'BackofficeUserEmail':
        return BackofficeUserEmail(value)

    @classmethod
    def random(cls) -> 'BackofficeUserEmail':
        return cls.create(cls.get_faker().random_user_email())

    @classmethod
    def invalid(cls) -> 'BackofficeUserEmail':
        return cls.create(cls.get_faker().invalid_user_email())
