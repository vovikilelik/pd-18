from flask import request
from flask_restx import Resource

from app.modules.api.misc.utils import resolve


def create_namespace(api, dao, *args):
    ns = api.namespace(*args)

    @ns.route('/')
    class List(Resource):

        @staticmethod
        def get_data():
            return dao.get_all(**request.args), 200

        def get(self):
            return resolve(self.get_data)

    @ns.route('/<int:element_id>')
    class Element(Resource):

        @staticmethod
        def get_data(element_id):
            return dao.get_by_index(element_id), 200

        def get(self, element_id):
            return resolve(lambda: self.get_data(element_id))

    return ns, List, Element
