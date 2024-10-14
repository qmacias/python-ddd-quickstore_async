from injector import Module, singleton, provider
from typing import Awaitable, Callable
from logging import Logger

from src.contexts.quickstore.users.application.UserCreator import UserCreator
from src.contexts.shared.infrastructure.persistence.MongoClientFactory import MongoClientFactory
from src.contexts.shared.infrastructure.persistence.MongoConfig import MongoConfig
from src.contexts.shared.domain.EventBus import EventBus

from src.contexts.quickstore.products.infrastructure.persistence.MongoProductRepository import MongoProductRepository
from src.contexts.quickstore.products.application.create.ProductCreator import ProductCreator
from src.contexts.quickstore.products.domain.ProductRepository import ProductRepository

from src.contexts.quickstore.users.infrastructure.MongoUserRepository import MongoUserRepository
from src.contexts.quickstore.users.domain.UserRepository import UserRepository


class QuickstoreModule(Module):
    @singleton
    @provider
    def quickstore_product_repository(self, config: MongoConfig) -> Callable[[], Awaitable[ProductRepository]]:
        async def __get_quickstore_product_repository() -> ProductRepository:
            client = await MongoClientFactory.create_client('products', config)

            return MongoProductRepository(client)

        return __get_quickstore_product_repository

    @singleton
    @provider
    def quickstore_product_creator(
            self,
            quickstore_repository_provider: Callable[[], Awaitable[ProductRepository]],
    ) -> Callable[[], Awaitable[ProductCreator]]:
        async def __get_quickstore_product_creator() -> ProductCreator:
            quickstore_repository = await quickstore_repository_provider()

            return ProductCreator(quickstore_repository)

        return __get_quickstore_product_creator

    @singleton
    @provider
    def quickstore_user_repository(self, config: MongoConfig) -> Callable[[], Awaitable[UserRepository]]:
        async def __get_quickstore_user_repository() -> UserRepository:
            client = await MongoClientFactory.create_client('users', config)

            return MongoUserRepository(client)

        return __get_quickstore_user_repository

    @singleton
    @provider
    def quickstore_user_creator(
            self,
            quickstore_repository_provider: Callable[[], Awaitable[UserRepository]],
            event_bus: EventBus,
            logger: Logger,
    ) -> Callable[[], Awaitable[UserCreator]]:
        async def __get_quickstore_user_creator() -> UserCreator:
            quickstore_repository = await quickstore_repository_provider()

            return UserCreator(quickstore_repository, event_bus, logger)

        return __get_quickstore_user_creator
