import json
from app import app

from .base_tests import BaseTestCase

class Tests_Offers(BaseTestCase):
    """Test for offers"""
    def test_add_offer_successfully(self):
        """Tests when the offers are submitted successfully"""
        with self.client:
            response = self.add_offer( "UAY905S","Bulenga", "kawempe", "9","3")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertEqual(data.get('message'), "Request successfully made and posted")
            response1 = self.add_offer( "UAY905S","Bulenga", "kawempe", "9","3")
            data1 = json.loads(response1.data.decode())
            self.assertEqual(response1.status_code, 201)
            self.assertEqual(data1.get('message'), "Request successfully made and posted")

    def test_get_all_offers(self):
        """Tests when all offers are retrieved successfully"""
        with self.client:
            self.add_offer("UAY905S","Bulenga", "kawempe", "9","3")
            response = self.get_offers()
            self.assertEqual(response.status_code, 404)

    def test_get_no_offers(self):
        """Tests when no offers are retrieved"""
        with self.client:
            self.add_offer("" ,"", "", "","")
            response = self.get_offers()
            self.assertEqual(response.status_code, 404)
     

    def test_edit_no_offer_by_id(self):
        """Tests when no offer is found by id when editing"""
        with self.client:
            self.add_offer(  "","", "","","")
            response = self.put_offer("UAY905S","Bulenga", "kawempe", "9","3")
            self.assertEqual(response.status_code, 405)

    def test_get_no_offer_by_id(self):
        """Tests when an offer is not found by id"""
        with self.client:
            self.add_offer( "", "", "","","")
            response = self.get_one_offer()
            self.assertEqual(response.status_code, 404)
