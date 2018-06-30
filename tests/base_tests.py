import unittest
import json
from app import app_config, app
from app.api.offers.views import offer_list
from app.api.requests.views import request_list

class BaseTestCase(unittest.TestCase):
    def create_app(self):
        """
        Create an instance of the app with the testing configuration
        """
        app.config.from_object(app_config["testing"])
        return app

    def setUp(self):
        self.client = app.test_client(self)

    def tearDown(self):
        """
        Drop the data structure data
        """
        request_list[:] = []
        offer_list[:]=[]

    def add_request(self, destination, setting_from, departure_time, seats_needed):
        """
        Function to create a request
        """
        return self.client.post(
            '/api/v1/requests',
            data=json.dumps(
                dict(
                    destination=destination,
                    setting_from=setting_from,
                    departure_time=departure_time,
                    seats_needed=seats_needed
                )
            ),
            content_type='application/json',
    
        )
    def get_requests(self):
        """
        function to return get
        """
        return self.client.get('/api/v1/requests')

    def get_one_request(self, id):
        """
        function to return get
        """
        return self.client.get('/api/v1/requests/{}'.format(id))

    def put_request(self,destination, setting_from, departure_time, seats_needed):
        """
        function to edit a request
        """
        return self.client.put('/api/v1/requests/{}'.format(id),
                               data=json.dumps(dict(
                                    destination=destination,
                                    setting_from=setting_from,
                                    departure_time=departure_time,
                                    seats_needed=seats_needed)),
                             content_type='application/json')

    
    def add_offer(self, number_plate,destination, setting_from, departure_time, seats_available):
        """
        Function to create an offer
        """
        return self.client.post(
            '/api/v1/offers',
            data=json.dumps(
                dict(
                    number_plate=number_plate,
                    destination=destination,
                    setting_from=setting_from,
                    departure_time=departure_time,
                    seats_available=seats_available
                )
            ),
            content_type='application/json'
        )
    def get_offers(self):
        """
        function to return get
        """
        return self.client.get('api/v1/offers')

    def get_one_offer(self, id):
        """
        function to return get
        """
        return self.client.get('api/v1/offers/{}'.format(id))

    def put_offer(self,id,number_plate,destination, setting_from, departure_time, seats_available):
        """
        function to edit an offer
        """
        return self.client.put('/api/v1/offers/{}'.format(id),
                               data=json.dumps(dict(
                                    number_plate=number_plate,
                                    destination=destination,
                                    setting_from=setting_from,
                                    departure_time=departure_time,
                                    seats_available=seats_available)),
                             content_type='application/json')