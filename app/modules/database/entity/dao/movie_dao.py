from app.modules.database.entity.dao.scheme.movie_scheme import movie_scheme, movie_list_scheme


class MovieDao:

    @classmethod
    def get_by_index(cls, idx):
        row = cls.query.get(idx)
        return movie_scheme.dump(row)

    @classmethod
    def get_all(cls):
        rows = cls.query.all()
        return movie_list_scheme.dump(rows)

    @classmethod
    def get_by(cls, **args):
        rows = cls.query.filter_by(**args).all()
        return movie_list_scheme.dump(rows)

    @classmethod
    def replace(cls, row):
        with cls.open() as session:
            session.add(row)
            session.commit()

            return movie_scheme.dump(row)

    @classmethod
    def remove(cls, value):
        rows = cls.get_by(**value)

        if len(rows) == 0:
            return False

        with cls.open() as session:
            session.delete(value)
            session.commit()

            return True
