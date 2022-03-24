from flask import request
from flask_restx import Resource

from app.modules.api.misc.utils import resolve


def create_namespace(api, dao, *args):
    movies_ns = api.namespace(*args)
    
    @movies_ns.route('/')
    class MoviesEndpoint(Resource):

        @staticmethod
        def get_data():
            return dao.get_by(**request.args), 200

        def get(self):
            return resolve(self.get_data)

        @staticmethod
        def add_data():
            data = request.json

            movie = dao(**data)
            dao.replace(movie)

            return movie

        def post(self):
            return resolve(self.add_data, error=400)

    @movies_ns.route('/<int:movie_id>')
    class MovieEndpoint(Resource):

        @staticmethod
        def get_data(movie_id):
            return dao.get_by_index(movie_id), 200

        def get(self, movie_id):
            return resolve(lambda: self.get_data(movie_id))

        @staticmethod
        def put_data(movie_id):
            data = request.json

            try:
                movie = dao(**data, id=movie_id)
                dao.replace(movie)
            except Exception as e:
                return 'Bad Request', 400

            return movie, 204

        @staticmethod
        def delete_data(movie_id):
            movie = dao.get_by_index(movie_id)

            if movie:
                dao.remove(movie)
                return 'Not Content', 204

        def put(self, movie_id):
            return resolve(lambda: self.change_data(movie_id))

        def delete(self, movie_id):
            return resolve(lambda: self.change_data(movie_id))
    
    return movies_ns, MoviesEndpoint, MovieEndpoint
