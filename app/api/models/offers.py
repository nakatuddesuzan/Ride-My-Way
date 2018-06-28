import uuid
import json


class Offer():
    def __init__(self, id, number_plate,destination, setting_from, departure_time,seats_available):
        self.id = id
        self.number_plate= number_plate
        self.destination= destination
        self.setting_from = setting_from
        self.departure_time = departure_time
        self.seats_available = seats_available

    def json(self):
        """
        json representation of the Offer model
        """
        return json.dumps({
            'id': self.id,
            'number_plate': self.number_plate,
            'destination': self.destination,
            'setting_from': self.setting_from,
            'departure_time':self.departure_time,
            'seats_available':self.seats_available
        })