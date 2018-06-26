from flask import Response
import json
from app.api.user_model.user import User
from tests.base_tests import BaseTestCase

from tests.base_tests import BaseTestCase
class Tests_Ride_offers(BaseTestCase):
    def test_add_offer_successfully(self):
        with self.client:
            response = self.add_ride_offer(  "her", "vgvg", "bbb","hygy","huhubh","hhuhu")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data.get('message'), "Ride offer successfully created")
            res = self.add_ride_offer("her", "vgvg", "bbb","hygy","huhubh","hhuhu")
            data1 = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 400)
            self.assertEqual(data1.get('message'), "Ride offer already created")
        

