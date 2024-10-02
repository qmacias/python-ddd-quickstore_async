from sqlalchemy import Column, String

from src.contexts.shared.infrastructure.Base import Base


class ProductModel(Base):
    __tablename__ = 'products'

    id = Column(String, primary_key=True)
    name = Column(String, unique=True, index=True)
