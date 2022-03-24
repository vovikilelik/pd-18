from flask_restx import Api

from app.modules.api.api_module import ApiModule
from app.modules.database.database_module import DatabaseModule
from lib.flask_app import FlaskApp, FlaskModule

DATABASE_PATH = './res/movies.db'


def create_app(import_name) -> FlaskApp:
    flask_app = FlaskApp(import_name)

    flask_app.add_module(
        DatabaseModule(f"sqlite:///{DATABASE_PATH}")
    ).add_module(
        ApiModule()
    )

    return flask_app
