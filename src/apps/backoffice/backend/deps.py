from logging import Logger

from injector import Module, singleton, provider

from sqlalchemy import create_engine, QueuePool
from sqlalchemy.orm import sessionmaker, Session

from src.contexts.shared.domain.EventBus import EventBus
from src.contexts.shared.infrastructure.Base import Base

from src.contexts.backoffice.users.infrastructure.sqlite.SQLiteBackofficeUserRepository import SQLiteBackofficeUserRepository
from src.contexts.backoffice.users.infrastructure.InMemoryBackofficeUserRepository import InMemoryBackofficeUserRepository
from src.contexts.backoffice.users.application.BackofficeUserCreator import BackofficeUserCreator
from src.contexts.backoffice.users.domain.BackofficeUserRepository import BackofficeUserRepository

from src.contexts.backoffice.products.infrastructure.sqlite.SQLiteBackofficeProductRepository import SQLiteBackofficeProductRepository
from src.contexts.backoffice.products.infrastructure.InMemoryBackofficeProductRepository import InMemoryBackofficeProductRepository
from src.contexts.backoffice.products.application.BackofficeProductCreator import BackofficeProductCreator
from src.contexts.backoffice.products.domain.BackofficeProductRepository import BackofficeProductRepository


class BackofficeModule(Module):
    @singleton
    @provider
    def sqlalchemy_engine(self) -> sessionmaker[Session]:
        # SQLALCHEMY_DATABASE_URL = 'sqlite:///./db/backoffice.db'
        SQLALCHEMY_DATABASE_URL = 'sqlite:///:memory:'

        engine = create_engine(
            SQLALCHEMY_DATABASE_URL,
            connect_args={'check_same_thread': False},
            poolclass=QueuePool,
            pool_size=5,
            max_overflow=10,
            pool_timeout=30,
            pool_recycle=1800,
        )

        Base.metadata.create_all(bind=engine)

        session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

        return session

    @singleton
    @provider
    def backoffice_user_repository(self, session: sessionmaker[Session]) -> BackofficeUserRepository:
        # backoffice_repository = InMemoryBackofficeUserRepository()
        backoffice_repository = SQLiteBackofficeUserRepository(session)

        return backoffice_repository

    @singleton
    @provider
    def backoffice_user_creator(
            self, backoffice_repository: BackofficeUserRepository, event_bus: EventBus, logger: Logger,
    ) -> BackofficeUserCreator:
        return BackofficeUserCreator(backoffice_repository, event_bus, logger)

    @singleton
    @provider
    def backoffice_product_repository(self, session: sessionmaker[Session]) -> BackofficeProductRepository:
        # backoffice_repository = InMemoryBackofficeProductRepository()
        backoffice_repository = SQLiteBackofficeProductRepository(session)

        return backoffice_repository

    @singleton
    @provider
    def backoffice_product_creator(
            self, backoffice_repository: BackofficeProductRepository, event_bus: EventBus, logger: Logger,
    ) -> BackofficeProductCreator:
        return BackofficeProductCreator(backoffice_repository, event_bus, logger)
