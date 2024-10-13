from logging import Logger

from src.contexts.shared.domain.EventBus import EventBus

from src.contexts.backoffice.users.domain.BackofficeUser import BackofficeUser
from src.contexts.backoffice.users.domain.BackofficeUserRepository import BackofficeUserRepository


class BackofficeUserCreator:
    def __init__(self, backoffice_repository: BackofficeUserRepository, event_bus: EventBus, logger: Logger) -> None:
        self.__backoffice_repository = backoffice_repository
        self.__eventbus = event_bus
        self.__logger = logger

    async def __call__(self, id: str, name: str, email: str) -> None:
        user = BackofficeUser.create(id, name, email)

        await self.__backoffice_repository.save(user)

        events = user.pull_domain_events()

        await self.__eventbus.publish(events)

        self.__logger.info(
            'Backoffice User Created',
            extra={'events': [event.to_primitives() for event in events]}
        )
