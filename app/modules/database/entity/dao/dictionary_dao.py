from app.modules.database.entity.dao.scheme.dict_scheme import dict_list_scheme, dict_scheme


class DictionaryDao:

    @classmethod
    def get_by_index(cls, idx):
        row = cls.query.get(idx)
        return dict_scheme.dump(row)

    @classmethod
    def get_all(cls):
        rows = cls.query.all()
        return dict_list_scheme.dump(rows)
