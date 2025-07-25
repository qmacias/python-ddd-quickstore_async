from injector import Module, singleton, provider
from typing import Awaitable, Callable
from logging import Logger

from src.contexts.shared.infrastructure.persistence.MongoClientFactory import MongoClientFactory
from src.contexts.shared.infrastructure.persistence.MongoConfig import MongoConfig
from src.contexts.shared.domain.EventBus import EventBus

from src.contexts.backoffice.products.infrastructure.persistence.MongoBackofficeProductRepository import MongoBackofficeProductRepository
from src.contexts.backoffice.products.application.BackofficeProductCreator import BackofficeProductCreator
from src.contexts.backoffice.products.domain.BackofficeProductRepository import BackofficeProductRepository

from src.contexts.backoffice.users.infrastructure.persistence.MongoBackofficeUserRepository import MongoBackofficeUserRepository
from src.contexts.backoffice.users.application.create.BackofficeUserCreator import BackofficeUserCreator
from src.contexts.backoffice.users.domain.BackofficeUserRepository import BackofficeUserRepository


class BackofficeModule(Module):
    @singleton
    @provider
    def backoffice_product_repository(self, config: MongoConfig) -> Callable[[], Awaitable[BackofficeProductRepository]]:
        async def __get_backoffice_product_repository() -> BackofficeProductRepository:
            client = await MongoClientFactory.create_client('backoffice-products', config)

            return MongoBackofficeProductRepository(client)

        return __get_backoffice_product_repository

    @singleton
    @provider
    def backoffice_product_creator(
            self,
            backoffice_repository_provider: Callable[[], Awaitable[BackofficeProductRepository]],
            event_bus: EventBus,
            logger: Logger,
    ) -> Callable[[], Awaitable[BackofficeProductCreator]]:
        async def __get_backoffice_product_creator() -> BackofficeProductCreator:
            backoffice_repository = await backoffice_repository_provider()

            return BackofficeProductCreator(backoffice_repository, event_bus, logger)

        return __get_backoffice_product_creator

    @singleton
    @provider
    def backoffice_user_repository(self, config: MongoConfig) -> Callable[[], Awaitable[BackofficeUserRepository]]:
        async def __get_backoffice_user_repository() -> BackofficeUserRepository:
            client = await MongoClientFactory.create_client('backoffice-users', config)

            return MongoBackofficeUserRepository(client)

        return __get_backoffice_user_repository

    @singleton
    @provider
    def backoffice_user_creator(
            self,
            backoffice_repository_provider: Callable[[], Awaitable[BackofficeUserRepository]],
    ) -> Callable[[], Awaitable[BackofficeUserCreator]]:
        async def __get_backoffice_user_creator() -> BackofficeUserCreator:
            backoffice_repository = await backoffice_repository_provider()

            return BackofficeUserCreator(backoffice_repository)

        return __get_backoffice_user_creator
