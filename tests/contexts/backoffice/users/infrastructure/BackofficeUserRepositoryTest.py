from unittest import IsolatedAsyncioTestCase

from src.apps.container import container
from src.contexts.backoffice.users.domain.BackofficeUserRepository import BackofficeUserRepository

from tests.contexts.shared.infrastructure.arranger.EnvironmentArranger import EnvironmentArranger
from tests.contexts.shared.domain.MotherCreator import MotherCreator
from tests.contexts.shared.domain.users.UserNameProvider import UserNameProvider
from tests.contexts.backoffice.users.domain.BackofficeUserMother import BackofficeUserMother


class BackofficeUserRepositoryTest(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.__arranger = container.get(EnvironmentArranger)

        await self.__arranger.arrange()

    async def test_should_save_a_backoffice_user(self) -> None:
        MotherCreator.add_provider(UserNameProvider)

        user = BackofficeUserMother.random()
        repository = container.get(BackofficeUserRepository)

        await repository.save(user)

    async def asyncTearDown(self):
        await self.__arranger.arrange()

        self.__arranger.close()
