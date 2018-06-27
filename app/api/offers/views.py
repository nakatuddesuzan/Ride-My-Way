from flask import jsonify, make_response,Flask
from flask_restful import Resource, reqparse

import re
import json

from app.api.models.offers import Offer


offer_list=[]
class AddOffer(Resource):
    id=0
    def post(self):
        """
        Allows to make ride offers
        """
        parser = reqparse.RequestParser()
        parser.add_argument('number_plate', type=str, required=True)
        parser.add_argument('destination', type=str, required=True)
        parser.add_argument('setting_from', type=str, required=True)
        parser.add_argument('departure_time', required=True)
        parser.add_argument('seats_available', type=str , required=False)
    
        args = parser.parse_args()
        number_plate = args['number_plate']
        destination = args['destination']
        setting_from = args['setting_from']
        departure_time= args['departure_time']
        seats_available= args['seats_available']
        
        global id
        if len(offer_list)==0:
            id = len(offer_list)+1
        else:
            id = id+1

        new_offer = Offer(id,number_plate, destination, setting_from, departure_time,seats_available)

        for offer in offer_list:
            if id == offer['id']:
                return make_response(jsonify({"message": '0ffer  already made'}), 400)
        offer = json.loads(new_offer.json())
        offer_list.append(offer)
        return make_response(jsonify({
            'message': 'Offer successfully made and poosted',
            'status': 'success'},
        ), 201)
    


class EditOffer(Resource):
    def put(self, offer_id):
        parser = reqparse.RequestParser()
        parser.add_argument('number_plate', type=str, required=True)
        parser.add_argument('destination', type=str, required=True)
        parser.add_argument('setting_from', type=str, required=True)
        parser.add_argument('departure_time', required=True)
        parser.add_argument('seats_available', type=int, required=False)
        args = parser.parse_args()
      

        for offer in offer_list:
            if int(offer['id']) == int(offer_id):
                args = parser.parse_args()
                offer['number_plate'] = args['number_plate']
                offer['destination'] = args['destination']
                offer['setting_from'] = args['setting_from']
                offer['departure_time'] = args['departure_time']
                offer['seats_available'] = args['seats_available']
                return make_response(jsonify({"message": "offer updated succesfully"}), 201)
        return make_response(jsonify({"message": "offer not found"}), 404)


class GetOffers(Resource):
    def get(self):
        my_offers = []
        for offer in offer_list:
            offers_data = {
                    "id": offer["id"],
                    "number_plate": offer['number_plate'],
                    "destination": offer['destination'],
                    "setting_from": offer['setting_from'],
                    "departure_time": offer['departure_time'],
                    "seats_available": offer['seats_available']
                }
            my_offers.append(offers_data)
        if my_offers:
            return make_response(jsonify({"offers": my_offers,
                                    "status": "success"}), 200)
        return make_response(jsonify({"message": "No requests found"}), 404)


class GetOneOffer(Resource):
    def get(self, offer_id):
        for offer in offer_list:
            if int(offer['id']) == int(offer_id):
                offers_data = {
                        "id": offer["id"],
                        "number_plate": offer['number_plate'],
                        "destination": offer['destination'],
                        "setting_from": offer['setting_from'],
                        "departure_time": offer['departure_time'],
                        "seats_available": offer['seats_available']
                    }
                return make_response(jsonify({"offers": offers_data,
                                    "status": "success"}), 200)
        return make_response(jsonify({"message": "No offers found"}), 404)