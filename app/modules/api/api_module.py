from flask_restx import Api

from app.modules.api.endpoint.dictionary import create_namespace as create_dict
from app.modules.api.endpoint.movies import create_namespace as create_movie
from app.modules.database.database_module import DatabaseModule
from app.modules.database.module.database_context import DatabaseContext
from lib.flask_app import FlaskModule


class ApiModule(FlaskModule):

    def init(self, flask_app, **modules):
        api = Api(flask_app.current)

        current_db: DatabaseContext = flask_app.get_module(DatabaseModule)

        create_movie(api, current_db.entity.movie, 'movies')
        create_dict(api, current_db.entity.genre, 'genres')
        create_dict(api, current_db.entity.director, 'directors')

        return api
