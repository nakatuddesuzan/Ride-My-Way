from flask import Flask
from flask import current_app
import unittest
import json
from app import app_config
from app import app
from app.api.rides.request_rides import requests
from app.api.user.views import user_list
from app.api.rides.add_rides import offers
    
class BaseTestCase(unittest.TestCase):
    def create_app(self):
        """
        Create an instance of the app with the testing configuration
        """
        current_app.config.from_object(app_config["testing"])
        return app

    def setUp(self):
        self.client = app.test_client(self)

    def tearDown(self):
        """
        Drop the data structure data
        """
        requests[:] = []
        user_list[:] = []
        offers[:] = []

    def SignUP(self, first_name, second_name, user_name, contact,email, password):
        return self.client.post('api/user/signup',
            data=json.dumps({'first_name':'first_name', 'second_name':'second_name', 'user_name':'user_name',
        'email': 'email','contact':'contact', 'password':'password' },content_type='application/json'
        )
                                )

    def login_user(self, email, password):
        """
        Method for logging a user with dummy data
        """
        return self.client.post('/api/user/login',
             data=json.dumps( { "email":"email","password":"password" } )
        )

           

    def get_user_token(self):
        """
        Returns a user token
        """
        response = self.login_user("sue@gmail.com", "1132018")
        data = json.loads(response.data.decode())
        return data['token']

    def add_ride_offer(self,driver_name, number_plate, destination,depature,departure_time,contact):
        """
        Function to create a request
        """
        return self.client.post( '/api/v1/rides/',
            data=json.dumps({'driver_name':'driver_name', 'number_plate':'number_plate', 'destination':'destination',
            'departure': 'departure' , 'departure_time':'departure_time', 'contact':'contact'})
            ,
            content_type='application/json'
        )

    def get_ride_offers(self, token):
        """
        function to return get
        """
        return self.client.get( headers=({"token": token}))

