from sqlalchemy import Column, String, Integer


class DictionaryMixin:
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
