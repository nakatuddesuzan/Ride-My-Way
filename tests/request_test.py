import json
from app import app

from .base_tests import BaseTestCase

class Tests_Requests(BaseTestCase):
    """Test for offers"""
    def test_add_request_successfully(self):
        """Tests when the requests are submitted successfully"""
        with self.client:
            response = self.add_request( "Bulenga", "kawempe", "9","3")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertEqual(data.get('message'), "Request successfully made and posted")
            response1 = self.add_request( "Bulenga", "kawempe", "9","3")
            data1 = json.loads(response1.data.decode())
            self.assertEqual(response1.status_code, 201)
            self.assertEqual(data1.get('message'), "Request successfully made and posted")

    def test_get_all_requests(self):
        """Tests when all requests are retrieved successfully"""
        with self.client:
            self.add_request("Bulenga", "kawempe", "9","3")
            response = self.get_requests()
            self.assertEqual(response.status_code, 404)

    def test_get_no_requests(self):
        """Tests when no requests are retrieved"""
        with self.client:
            response = self.get_requests()
            self.assertEqual(response.status_code, 404)

    def test_get_no_request_by_id(self):
        """Tests when a request is not found by id"""
        with self.client:
            response = self.get_one_request(1)
            self.assertEqual(response.status_code, 404)

    
    def test_if_request_was_added_by_id(self):
        """Tests if a request was added"""
        with self.client:
            new_request = self.add_request("Bulenga", "kawempe", "9", "3")
            new_request_id = json.loads(new_request.data).get("id")
            self.assertEqual(new_request_id, 1)
