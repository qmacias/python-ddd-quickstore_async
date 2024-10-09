from injector import Module, singleton, provider
from typing import Awaitable, Callable
from logging import Logger

from settings import settings

from src.contexts.shared.domain.EventBus import EventBus

from src.contexts.shared.infrastructure.persistence.MongoConfig import MongoConfig
from src.contexts.shared.infrastructure.persistence.MongoClientFactory import MongoClientFactory

from src.contexts.backoffice.users.infrastructure.persistence.MongoBackofficeUserRepository import MongoBackofficeUserRepository
from src.contexts.backoffice.users.application.BackofficeUserCreator import BackofficeUserCreator
from src.contexts.backoffice.users.domain.BackofficeUserRepository import BackofficeUserRepository

from src.contexts.backoffice.products.infrastructure.persistence.MongoBackofficeProductRepository import MongoBackofficeProductRepository
from src.contexts.backoffice.products.application.BackofficeProductCreator import BackofficeProductCreator
from src.contexts.backoffice.products.domain.BackofficeProductRepository import BackofficeProductRepository

from tests.contexts.shared.infrastructure.arranger.EnvironmentArranger import EnvironmentArranger
from tests.contexts.shared.infrastructure.arranger.MongoEnvironmentArranger import MongoEnvironmentArranger


class BackofficeModule(Module):
    @singleton
    @provider
    def config(self) -> MongoConfig:
        config = MongoConfig(uri=settings.MONGODB_URI)

        return config

    @singleton
    @provider
    def environment_arranger(self, config: MongoConfig) -> EnvironmentArranger:
        arranger = MongoEnvironmentArranger(config.uri, 'backoffice')

        return arranger

    @singleton
    @provider
    def backoffice_user_repository(self, config: MongoConfig) -> Callable[[], Awaitable[BackofficeUserRepository]]:
        async def __get_backoffice_user_repository() -> BackofficeUserRepository:
            client = await MongoClientFactory.create_client('backoffice-user', config)

            return MongoBackofficeUserRepository(client)

        return __get_backoffice_user_repository

    @singleton
    @provider
    def backoffice_user_creator(
            self,
            backoffice_repository_provider: Callable[[], Awaitable[BackofficeUserRepository]],
            event_bus: EventBus,
            logger: Logger,
    ) -> Callable[[], Awaitable[BackofficeUserCreator]]:
        async def __get_backoffice_user_creator() -> BackofficeUserCreator:
            repository = await backoffice_repository_provider()

            return BackofficeUserCreator(repository, event_bus, logger)

        return __get_backoffice_user_creator

    @singleton
    @provider
    def backoffice_product_repository(self, config: MongoConfig) -> Callable[[], Awaitable[BackofficeProductRepository]]:
        async def __get_backoffice_product_repository() -> BackofficeProductRepository:
            client = await MongoClientFactory.create_client('backoffice-product', config)

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
            repository = await backoffice_repository_provider()

            return BackofficeProductCreator(repository, event_bus, logger)

        return __get_backoffice_product_creator
