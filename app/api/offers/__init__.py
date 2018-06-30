from flask import Blueprint
from flask_restful import Api
from .views import AddOffer, EditOffer, GetOffers, GetOneOffer

offer = Blueprint('offers', __name__)
api = Api(offer)
api.add_resource(AddOffer, '/api/v1/offers')
api.add_resource(GetOffers, '/api/v1/offers')
api.add_resource(GetOneOffer, '/api/v1/offers/<offer_id>')
api.add_resource(EditOffer, '/api/v1/<offer_id>')