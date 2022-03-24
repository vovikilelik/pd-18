from app.modules.database.entity.director import create_entity as create_director
from app.modules.database.entity.genre import create_entity as create_genre
from app.modules.database.entity.movie import create_entity as create_movie


class EntrySet:

    def __init__(self, base):
        self._director = create_director(base)
        self._genre = create_genre(base)
        self._movie = create_movie(base)

    @property
    def director(self):
        return self._director

    @property
    def genre(self):
        return self._genre

    @property
    def movie(self):
        return self._movie
