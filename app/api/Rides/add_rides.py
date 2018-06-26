from flask import Flask, jsonify, request,make_response, abort
from datetime import datetime
from app import app

DEBUG = True
HOST= '0.0.0.0'
PORT='5000'


offers = []

global id
id=0
if len(offers)==0:
    id = len(offers)+1
else:
    id = id+1
    
@app.route('/api/v1/rides', methods=['GET'])
def get_offer(self):
    return jsonify(offers)

@app.route('/api/v1/rides/<int:ride_id>', methods=['GET'])
def get_offer_id(ride_id):
    print('drivers')
    for offers in offers:
        if int(offers['id'])== int(ride_id):

            offer_data={
                "ride_id": offers["id"],
                "driver_name": offers['driver_name'],
                "plate":offers['number_plate'],
                "destination":offers["destination"],
                "departure":offers["departure"],
                "departure_time":offers["departure_time"],
                "contact":offers(["contact"] ,type=int)
            }

            return jsonify(offer_data)
        else:
            abort(400)
    

    

@app.route('/api/v1/rides', methods=['POST'])
def add_offer():
    driver_name = request.json['driver_name']
    plate = request.json['number_plate']
    destination = request.json['destination']
    departure = request.json['departure']
    departure_time = request.json['departure_time']
    contact = request.json['contact']
    offers.append({'driver_name':driver_name, 'number_plate':plate, 'destination':destination,
    'departure': departure , 'departure_time':departure_time, 'contact':contact})
    
    return jsonify(offers),201
