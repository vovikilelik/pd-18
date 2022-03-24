from app.modules.database.module.database_context import DatabaseContext
from app.modules.database.module.static_vars import CONNECT_ARGS
from lib.flask_app import FlaskModule


class DatabaseModule(FlaskModule):

    def __init__(self, database_url):
        self._database_url = database_url

    def init(self, flask_app, **modules) -> DatabaseContext:
        return DatabaseContext(self._database_url, connect_args=CONNECT_ARGS)
