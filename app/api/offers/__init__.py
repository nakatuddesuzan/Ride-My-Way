from flask import Blueprint
from flask_restful import Api
from .views import AddOffer, EditOffer, GetOffers, GetOneOffer

offer = Blueprint('offers', __name__)
maintainance_api = Api(offer)
maintainance_api.add_resource(AddOffer, '/api/v1/offers')
maintainance_api.add_resource(GetOffers, '/api/v1/offers')
maintainance_api.add_resource(GetOneOffer, '/api/v1/offers/<offer_id>')
maintainance_api.add_resource(EditOffer, '/api/v1/<offer_id>')