from src.contexts.backoffice.users.domain.BackofficeUser import BackofficeUser

from tests.contexts.backoffice.users.domain.BackofficeUserIdMother import BackofficeUserIdMother
from tests.contexts.backoffice.users.domain.BackofficeUserNameMother import BackofficeUserNameMother
from tests.contexts.backoffice.users.domain.BackofficeUserEmailMother import BackofficeUserEmailMother


class BackofficeUserMother:
    @staticmethod
    def create(
            id: str,
            name: str,
            email: str,
    ) -> 'BackofficeUser':
        return BackofficeUser.create(
            BackofficeUserIdMother.create(id).value,
            BackofficeUserNameMother.create(name).value,
            BackofficeUserEmailMother.create(email).value,
        )

    @classmethod
    def random(cls) -> 'BackofficeUser':
        return cls.create(
            BackofficeUserIdMother.random().value,
            BackofficeUserNameMother.random().value,
            BackofficeUserEmailMother.random().value,
        )
