from app.modules.database.entity.dao.dictionary_dao import DictionaryDao
from app.modules.database.entity.mixins.dictionary_mixin import DictionaryMixin


def create_entity(base):
    class Genre(DictionaryMixin, DictionaryDao, base):
        __tablename__ = 'genre'

    return Genre
