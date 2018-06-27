from flask import jsonify, make_response
from flask_restful import Resource, reqparse

import re
import json

from app.api.models.requests import Request



request_list=[]
class AddRequest(Resource):
    id=0
    def post(self):
        """
        Allows
         to make a ride request
        """
        parser = reqparse.RequestParser()
        parser.add_argument('destination', type=str, required=True)
        parser.add_argument('setting_from', type=str, required=True)
        parser.add_argument('departure_time', required=True)
        parser.add_argument('seats_needed', type=int , required=False)
        
        args = parser.parse_args()
        destination = args['destination']
        setting_from = args['setting_from']
        departure_time= args['departure_time']
        seats_needed= args['seats_needed']
        
        global id
        if len(request_list)==0:
            id = len(request_list)+1
        else:
            id = id+1

        new_request = Request(id, destination, setting_from, departure_time,seats_needed)

        for request in request_list:
            if id == request['id']:
                return make_response(jsonify({"message": 'Request successfully made and posted'}), 400)
        request = json.loads(new_request.json())
        request_list.append(request)
        return make_response(jsonify({
            'message': 'Request successfully made and posted',
            'status': 'success'},
        ), 201)


class EditRequest(Resource):
    def put(self, request_id):
        parser = reqparse.RequestParser()
        parser.add_argument('destination', type=str, required=True)
        parser.add_argument('setting_from', type=str, required=True)
        parser.add_argument('departure_time', type=str, required=True)
        parser.add_argument('seats_needed', type=str, required=True)
        
        args = parser.parse_args()
        for request in request_list:
            if int(request['id']) == int(request_id):
                args = parser.parse_args()
                request['destination'] = args['destination']
                request['setting_from'] = args['setting_from']
                request['departure_time'] = args['departure_time']
                request['seats_needed'] = args['seats_needed']
                return make_response(jsonify({"message": "request updated succesfully"}), 201)
       


class GetRequests(Resource):
    def get(self):
        my_requests = []
        for request in request_list:
            requests_data = {
                    "id": request["id"],
                    "destination": request['destination'],
                    "setting_from": request['setting_from'],
                    "departure_time": request['departure_time'],
                    "seats_needed": request['seats_needed']
                }
            my_requests.append(requests_data)
        if my_requests:
            return make_response(jsonify({"requests": my_requests,
                                    "status": "success"}), 200)
        return make_response(jsonify({"message": "No requests found"}), 404)


class GetOneRequest(Resource):
    def get(self, request_id):
        for request in request_list:
            if int(request['id']) == int(request_id):
                requests_data = {
                        "id": request["id"],
                        "destination": request['destination'],
                        "setting_from": request['setting_from'],
                        "departure_time": request['departure_time'],
                        "seats_needed": request['seats_needed']
                    }
                return make_response(jsonify({"requests": requests_data,
                                    "status": "success"}), 200)
        return make_response(jsonify({"message": "No requests found"}), 404)