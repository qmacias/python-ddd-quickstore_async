from sqlalchemy import Column, String

from src.contexts.shared.infrastructure.Base import Base


class BackofficeUserModel(Base):
    __tablename__ = 'backoffice_users'

    id = Column(String, primary_key=True)
    name = Column(String, unique=True, index=True)
