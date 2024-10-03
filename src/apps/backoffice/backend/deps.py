from logging import Logger

from injector import Module, singleton, provider

from src.contexts.shared.domain.EventBus import EventBus

from src.contexts.backoffice.users.infrastructure.persistence.InMemoryBackofficeUserRepository import InMemoryBackofficeUserRepository
from src.contexts.backoffice.users.application.BackofficeUserCreator import BackofficeUserCreator
from src.contexts.backoffice.users.domain.BackofficeUserRepository import BackofficeUserRepository

from src.contexts.backoffice.products.infrastructure.persistence.InMemoryBackofficeProductRepository import InMemoryBackofficeProductRepository
from src.contexts.backoffice.products.application.BackofficeProductCreator import BackofficeProductCreator
from src.contexts.backoffice.products.domain.BackofficeProductRepository import BackofficeProductRepository


class BackofficeModule(Module):
    @singleton
    @provider
    def backoffice_user_repository(self) -> BackofficeUserRepository:
        backoffice_repository = InMemoryBackofficeUserRepository()

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
        backoffice_repository = InMemoryBackofficeProductRepository()

        return backoffice_repository

    @singleton
    @provider
    def backoffice_product_creator(
            self, backoffice_repository: BackofficeProductRepository, event_bus: EventBus, logger: Logger,
    ) -> BackofficeProductCreator:
        return BackofficeProductCreator(backoffice_repository, event_bus, logger)
