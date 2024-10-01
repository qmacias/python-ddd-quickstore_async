from tests.contexts.shared.domain.MotherCreator import MotherCreator

from src.contexts.backoffice.users.domain.BackofficeUserName import BackofficeUserName


class BackofficeUserNameMother(MotherCreator):
    @staticmethod
    def create(
            value: str,
    ) -> 'BackofficeUserName':
        return BackofficeUserName(value)

    @classmethod
    def random(cls) -> 'BackofficeUserName':
        return cls.create(cls.get_faker().random_user_name())

    @classmethod
    def invalid(cls) -> 'BackofficeUserName':
        return cls.create(cls.get_faker().invalid_user_name())
