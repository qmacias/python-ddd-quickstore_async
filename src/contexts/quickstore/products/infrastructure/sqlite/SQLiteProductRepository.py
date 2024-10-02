from contextlib import contextmanager

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, Session

from src.contexts.quickstore.products.infrastructure.sqlite.ProductModel import ProductModel
from src.contexts.quickstore.products.domain.Product import Product
from src.contexts.quickstore.products.domain.ProductRepository import ProductRepository


class SQLiteProductRepository(ProductRepository):
    def __init__(self, session: sessionmaker[Session]) -> None:
        self.__local_session = session

    @contextmanager
    def get_session(self):
        session = self.__local_session()
        try:
            yield session
            session.commit()
        except SQLAlchemyError:
            session.rollback()
            raise
        finally:
            session.close()

    async def save(self, product: Product) -> None:
        with self.get_session() as session:
            db_product = ProductModel(
                id=product.id.value, name=product.name.value,
            )

            session.merge(db_product)
