from app.modules.database.entity.dao.movie_dao import MovieDao
from app.modules.database.entity.mixins.movie_mixin import MovieMixin


def create_entity(base):
    class Movie(MovieMixin, MovieDao, base):
        __tablename__ = 'movie'

    return Movie
