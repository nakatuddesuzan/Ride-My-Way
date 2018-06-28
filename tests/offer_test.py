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
            self.assertEqual(data.get('message'), "Offer successfully made and posted")
            response1 = self.add_offer( "UAY905S","Bulenga", "kawempe", "9","3")
            data1 = json.loads(response1.data.decode())
            self.assertEqual(response1.status_code, 201)
            self.assertEqual(data1.get('message'), "Offer successfully made and posted")

    def test_get_all_offers(self):
        """Tests when all offers are retrieved successfully"""
        with self.client:
            self.add_offer("UAY905S","Bulenga", "kawempe", "9","3")
            response = self.get_offers()
            self.assertEqual(response.status_code, 200)

    def test_get_no_offers(self):
        """Tests when no offers are retrieved"""
        with self.client:
            self.add_offer("" ,"", "", "","")
            response = self.get_offers()
            self.assertEqual(response.status_code, 200)

    def test_get_no_offer_by_id(self):
        """Tests when an offer is not found by id"""
        with self.client:
            response = self.get_one_offer(1)
            self.assertEqual(response.status_code, 404)

    
    def test_get_offer_by_id(self):
        """Tests if an offer can be get by an id"""
        with self.client:
            new_offer = self.add_offer("UAY905S", "Bulenga", "kawempe", "9", "3")
            new_offer_id = json.loads(new_offer.data).get("id")
            new_offer1 = self.add_offer("UAY905S", "Bulenga", "kawempe", "5", "3")
            new_offer_id1 = json.loads(new_offer1.data).get("id")
            self.assertListEqual([new_offer_id, new_offer_id1], [1, 2])
