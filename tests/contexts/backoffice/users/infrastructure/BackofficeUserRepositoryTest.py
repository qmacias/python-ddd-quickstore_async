from unittest import TestCase

from src.apps.container import container
from src.contexts.backoffice.users.domain.BackofficeUserRepository import BackofficeUserRepository

from tests.contexts.shared.infrastructure.async_test import async_test
from tests.contexts.shared.domain.MotherCreator import MotherCreator
from tests.contexts.shared.domain.users.UserNameProvider import UserNameProvider
from tests.contexts.backoffice.users.domain.BackofficeUserMother import BackofficeUserMother


class BackofficeUserRepositoryTest(TestCase):
    def setUp(self) -> None:
        MotherCreator.add_provider(UserNameProvider)

        self.__repository = container.get(BackofficeUserRepository)

    @async_test
    async def test_should_save_a_backoffice_user(self) -> None:
        user = BackofficeUserMother.random()

        await self.__repository.save(user)
