import uuid
import json


class Request():
    def __init__(self, id, destination, setting_from, departure_time,seats_needed):
        self.id = id
        self.destination= destination
        self.setting_from = setting_from
        self.departure_time = departure_time
        self.seats_needed = seats_needed

    def json(self):
        """
        json representation of the Request model
        """
        return json.dumps({
            'id': self.id,
            'destination': self.destination,
            'setting_from': self.setting_from,
            'departure_time':self.departure_time,
            'seats_needed':self.seats_needed
        })