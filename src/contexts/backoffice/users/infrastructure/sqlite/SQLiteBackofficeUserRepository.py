from contextlib import contextmanager

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, Session

from src.contexts.backoffice.users.infrastructure.sqlite.BackofficeUserModel import BackofficeUserModel
from src.contexts.backoffice.users.domain.BackofficeUserRepository import BackofficeUserRepository
from src.contexts.backoffice.users.domain.BackofficeUser import BackofficeUser


class SQLiteBackofficeUserRepository(BackofficeUserRepository):
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

    async def save(self, user: BackofficeUser) -> None:
        with self.get_session() as session:
            db_user = BackofficeUserModel(
                id=user.id.value, name=user.name.value,
            )

            session.merge(db_user)
