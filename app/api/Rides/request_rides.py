from flask import Flask, jsonify, request,make_response, abort
from app import app

DEBUG = True
HOST= '0.0.0.0'
PORT='5000'

requests=[]
@app.route('/api/v1/request', methods=['GET'])
def get_requests():
    return jsonify(requests)

@app.route('/api/v1/request', methods=['POST'])
def add_request():

    passenger_name = request.json[' passenger_name']
    destination = request.json['destination']
    departure = request.json['departure']
    departure_time = request.json['departure_time']
    seats_needed = request.json['seats_needed']

    requests.append({' passenger_name': passenger_name, 'destination':destination, 'departure': departure ,
        'departure_time':departure_time, 'seats_needed':seats_needed})
    return jsonify(requests)

