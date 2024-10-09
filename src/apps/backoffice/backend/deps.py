from logging import Logger
from injector import Module, singleton, provider

from src.contexts.shared.domain.EventBus import EventBus
from src.apps.backoffice.backend.settings import settings

from src.contexts.backoffice.users.infrastructure.persistence.MongoBackofficeUserRepository import MongoBackofficeUserRepository
from src.contexts.backoffice.users.application.BackofficeUserCreator import BackofficeUserCreator
from src.contexts.backoffice.users.domain.BackofficeUserRepository import BackofficeUserRepository

from src.contexts.backoffice.products.infrastructure.persistence.MongoBackofficeProductRepository import MongoBackofficeProductRepository
from src.contexts.backoffice.products.application.BackofficeProductCreator import BackofficeProductCreator
from src.contexts.backoffice.products.domain.BackofficeProductRepository import BackofficeProductRepository

from tests.contexts.shared.infrastructure.arranger.EnvironmentArranger import EnvironmentArranger
from tests.contexts.shared.infrastructure.arranger.MongoEnvironmentArranger import MongoEnvironmentArranger

BACKOFFICE_MONGODB_URI = settings.MONGODB_URI


class BackofficeModule(Module):
    @singleton
    @provider
    def environment_arranger(self) -> EnvironmentArranger:
        return MongoEnvironmentArranger(BACKOFFICE_MONGODB_URI, 'backoffice')

    @singleton
    @provider
    def backoffice_user_repository(self) -> BackofficeUserRepository:
        # backoffice_repository = InMemoryBackofficeUserRepository()
        backoffice_repository = MongoBackofficeUserRepository(BACKOFFICE_MONGODB_URI)

        return backoffice_repository

    @singleton
    @provider
    def backoffice_user_creator(
            self, backoffice_repository: BackofficeUserRepository, event_bus: EventBus, logger: Logger,
    ) -> BackofficeUserCreator:
        return BackofficeUserCreator(backoffice_repository, event_bus, logger)

    @singleton
    @provider
    def backoffice_product_repository(self) -> BackofficeProductRepository:
        # backoffice_repository = InMemoryBackofficeProductRepository()
        backoffice_repository = MongoBackofficeProductRepository(BACKOFFICE_MONGODB_URI)

        return backoffice_repository

    @singleton
    @provider
    def backoffice_product_creator(
            self, backoffice_repository: BackofficeProductRepository, event_bus: EventBus, logger: Logger,
    ) -> BackofficeProductCreator:
        return BackofficeProductCreator(backoffice_repository, event_bus, logger)
