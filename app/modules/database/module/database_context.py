from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session

from app.modules.database.module.entry_set import EntrySet


class Session:
    def __init__(self, session_context):
        self._session_context = session_context

    def __enter__(self):
        return self._session_context

    def __exit__(self, exc_type, exc_value, traceback):
        self._session_context.close()


class DatabaseContext:
    def __init__(self, database_url, **args):
        engine = create_engine(
            database_url,
            **args
        )

        self._session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

        base = declarative_base()
        base.query = self._session.query_property()
        base.open = self.open

        self._entity = EntrySet(base)
        base.metadata.create_all(bind=engine)

    @property
    def session(self):
        return self._session

    @property
    def entity(self) -> EntrySet:
        return self._entity

    def open(self):
        return Session(self._session())
