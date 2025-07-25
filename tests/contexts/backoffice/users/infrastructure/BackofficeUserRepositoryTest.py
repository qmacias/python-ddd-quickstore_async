from typing import Callable, Awaitable
from unittest import IsolatedAsyncioTestCase

from src.apps.container import container

from src.contexts.backoffice.users.domain.BackofficeUserRepository import BackofficeUserRepository

from tests.contexts.shared.infrastructure.arranger.EnvironmentArranger import EnvironmentArranger
from tests.contexts.shared.domain.MotherCreator import MotherCreator
from tests.contexts.shared.domain.users.UserNameProvider import UserNameProvider
from tests.contexts.shared.domain.users.UserEmailProvider import UserEmailProvider
from tests.contexts.backoffice.users.domain.BackofficeUserMother import BackofficeUserMother


class BackofficeUserRepositoryTest(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        arranger_provider = container.get(
            Callable[[], Awaitable[EnvironmentArranger]],
        )

        self.__arranger = await arranger_provider()

        await self.__arranger.arrange()

    async def test_should_be_able_to_persist_the_same_backoffice_user_twice(self) -> None:
        MotherCreator.add_provider(UserNameProvider)
        MotherCreator.add_provider(UserEmailProvider)

        user = BackofficeUserMother.random()

        repository_provider = container.get(
            Callable[[], Awaitable[BackofficeUserRepository]],
        )

        repository = await repository_provider()

        await repository.save(user)
        await repository.save(user)

        persisted_users = await repository.search_all()

        self.assertEqual(len(persisted_users), 1)
        self.assertEqual(persisted_users, [user])

    async def asyncTearDown(self):
        await self.__arranger.arrange()

        self.__arranger.close()
