from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock

from src.contexts.backoffice.users.application.create.BackofficeUserCreator import BackofficeUserCreator
from src.contexts.backoffice.users.domain.BackofficeUserRepository import BackofficeUserRepository

from tests.contexts.shared.domain.MotherCreator import MotherCreator
from tests.contexts.shared.domain.users.UserNameProvider import UserNameProvider
from tests.contexts.shared.domain.users.UserEmailProvider import UserEmailProvider
from tests.contexts.backoffice.users.domain.BackofficeUserMother import BackofficeUserMother


class BackofficeUserCreatorTest(IsolatedAsyncioTestCase):
    async def test_creates_a_backoffice_user(self) -> None:
        MotherCreator.add_provider(UserNameProvider)
        MotherCreator.add_provider(UserEmailProvider)

        user = BackofficeUserMother.random()

        repository = AsyncMock(spec=BackofficeUserRepository)
        application_service = BackofficeUserCreator(repository)

        await application_service(str(user.id), str(user.name), str(user.email))

        repository.save.assert_called_once_with(user)
