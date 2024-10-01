from src.contexts.backoffice.users.domain.BackofficeUser import BackofficeUser

from tests.contexts.backoffice.users.domain.BackofficeUserIdMother import BackofficeUserIdMother
from tests.contexts.backoffice.users.domain.BackofficeUserNameMother import BackofficeUserNameMother


class BackofficeUserMother:
    @staticmethod
    def create(
            id: str,
            name: str,
    ) -> 'BackofficeUser':
        return BackofficeUser.create(
            BackofficeUserIdMother.create(id).value,
            BackofficeUserNameMother.create(name).value,
        )

    @classmethod
    def random(cls) -> 'BackofficeUser':
        return cls.create(
            BackofficeUserIdMother.random().value,
            BackofficeUserNameMother.random().value,
        )

    @staticmethod
    def create_without_events(
            id: str,
            name: str,
    ) -> 'BackofficeUser':
        return BackofficeUser(
            BackofficeUserIdMother.create(id),
            BackofficeUserNameMother.create(name),
        )

    @staticmethod
    def random_without_events() -> 'BackofficeUser':
        return BackofficeUser(
            BackofficeUserIdMother.random(),
            BackofficeUserNameMother.random(),
        )

    @classmethod
    def with_bad_id(cls) -> 'BackofficeUser':
        return cls.create(
            BackofficeUserIdMother.invalid().value,
            BackofficeUserNameMother.random().value,
        )

    @classmethod
    def with_bad_name(cls) -> 'BackofficeUser':
        return cls.create(
            BackofficeUserIdMother.random().value,
            BackofficeUserNameMother.invalid().value,
        )
