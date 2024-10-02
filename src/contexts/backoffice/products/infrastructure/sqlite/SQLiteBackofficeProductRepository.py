from contextlib import contextmanager

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, Session

from src.contexts.backoffice.products.infrastructure.sqlite.BackofficeProductModel import BackofficeProductModel
from src.contexts.backoffice.products.domain.BackofficeProductRepository import BackofficeProductRepository
from src.contexts.backoffice.products.domain.BackofficeProduct import BackofficeProduct


class SQLiteBackofficeProductRepository(BackofficeProductRepository):
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

    async def save(self, product: BackofficeProduct) -> None:
        with self.get_session() as session:
            db_product = BackofficeProductModel(
                id=product.id.value, name=product.name.value,
            )

            session.merge(db_product)
