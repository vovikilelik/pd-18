from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declared_attr


class MovieMixin:
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    trailer = Column(String)
    year = Column(Integer)
    rating = Column(Integer)

    @declared_attr
    def genre_id(self):
        return Column(Integer, ForeignKey('genre.id'))

    @declared_attr
    def director_id(self):
        return Column(Integer, ForeignKey('director.id'))
