from flask import Blueprint
from flask_restful import Api
from .views import AddRequest, EditRequest, GetRequests, GetOneRequest

request = Blueprint('requests', __name__)
api = Api(request)
api.add_resource(AddRequest, '/api/v1/requests')
api.add_resource(GetRequests, '/api/v1/requests')
api.add_resource(GetOneRequest, '/api/v1/requests/<request_id>')
api.add_resource(EditRequest, '/api/v1/requests/<request_id>')