from logging import Logger

from src.contexts.shared.domain.EventBus import EventBus

from src.contexts.quickstore.users.domain.User import User
from src.contexts.quickstore.users.domain.UserRepository import UserRepository


class UserCreator:
    def __init__(self, repository: UserRepository, eventbus: EventBus, logger: Logger) -> None:
        self.__repository = repository
        self.__eventbus = eventbus
        self.__logger = logger

    async def __call__(self, id: str, name: str, email: str) -> None:
        user = User.create(id, name, email)

        await self.__repository.save(user)

        events = user.pull_domain_events()

        await self.__eventbus.publish(events)

        self.__logger.info(
            'User Created',
            extra={'events': [event.to_primitives() for event in events]}
        )
