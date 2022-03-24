from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declared_attr


class BaseMixin:

    @declared_attr
    def __tablename__(self):
        return self.__name__.lower()

    id = Column(Integer, primary_key=True)
