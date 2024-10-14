from src.contexts.backoffice.users.domain.BackofficeUser import BackofficeUser
from src.contexts.backoffice.users.domain.BackofficeUserRepository import BackofficeUserRepository


class BackofficeUserCreator:
    def __init__(self, backoffice_repository: BackofficeUserRepository) -> None:
        self.__backoffice_repository = backoffice_repository

    async def __call__(self, id: str, name: str, email: str) -> None:
        user = BackofficeUser.create(id, name, email)

        await self.__backoffice_repository.save(user)
