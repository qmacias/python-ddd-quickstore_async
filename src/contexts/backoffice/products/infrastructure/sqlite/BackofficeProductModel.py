from sqlalchemy import Column, String

from src.contexts.shared.infrastructure.Base import Base


class BackofficeProductModel(Base):
    __tablename__ = 'backoffice_products'

    id = Column(String, primary_key=True)
    name = Column(String, unique=True, index=True)
