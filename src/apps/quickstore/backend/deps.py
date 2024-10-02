from injector import Module, singleton, provider, multiprovider, inject

from sqlalchemy import create_engine, QueuePool
from sqlalchemy.orm import sessionmaker, Session

from src.contexts.shared.infrastructure.Base import Base
from src.contexts.shared.domain.EventSubscriber import EventSubscriber

from src.contexts.quickstore.products.infrastructure.sqlite.SQLiteProductRepository import SQLiteProductRepository
from src.contexts.quickstore.products.infrastructure.InMemoryProductRepository import InMemoryProductRepository
from src.contexts.quickstore.products.application.create.CreateProductOnBackofficeProductCreated import CreateProductOnBackofficeProductCreated
from src.contexts.quickstore.products.application.create.ProductCreator import ProductCreator
from src.contexts.quickstore.products.domain.ProductRepository import ProductRepository


class QuickstoreModule(Module):
    @singleton
    @provider
    def sqlalchemy_engine(self) -> sessionmaker[Session]:
        # SQLALCHEMY_DATABASE_URL = 'sqlite:///./db/quickstore.db'
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
    def product_repository(self, session: sessionmaker[Session]) -> ProductRepository:
        repository = InMemoryProductRepository()
        # repository = SQLiteProductRepository(session)

        return repository

    @singleton
    @provider
    def product_creator(
            self, repository: ProductRepository,
    ) -> ProductCreator:
        return ProductCreator(repository)

    @singleton
    @provider
    def create_product_on_backoffice_product_created_subscriber(
            self, creator: ProductCreator,
    ) -> EventSubscriber:
        return CreateProductOnBackofficeProductCreated(creator)


class QuickstoreEventSubscribersModule(Module):
    @singleton
    @multiprovider
    @inject
    def event_subscribers(
            self,
            creator: ProductCreator,
    ) -> list[EventSubscriber]:
        return [
            CreateProductOnBackofficeProductCreated(creator),
        ]

