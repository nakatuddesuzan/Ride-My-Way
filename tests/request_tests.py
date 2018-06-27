import json
from app import app
from .base_tests import BaseTestCase

class Tests_Requests(BaseTestCase):
    """Test for requests"""
    def test_add_request_successfully(self):
        """Tests when the requests are submitted successfully"""
        with self.client:
            response = self.add_request("Bulenga", "kawempe", "9","5")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertEqual(data.get('message'), "Request successfully created and sent")
            response1 = self.add_request("Bulenga", "kawempe", "9","5")
            data1 = json.loads(response1.data.decode())
            self.assertEqual(response1.status_code, 201)
            self.assertEqual(data1.get('message'), "Request already exists")

    def test_get_all_requests(self):
        """Tests when all requests are retrieved successfully"""
        with self.client:
            self.add_request("Bulenga", "kawempe", "9","5")
            response = self.get_requests()
            self.assertEqual(response.status_code, 404)

    def test_get_no_requests(self):
        """Tests when no requests are retrieved"""
        with self.client:
            self.add_request( "", "", "","")
            response = self.get_requests()
            self.assertEqual(response.status_code, 404)

    def test_get_no_request_by_id(self):
        """Tests when a request is not found by id"""
        with self.client:
            self.add_request("", "", "","")
            response = self.get_one_request()
            self.assertEqual(response.status_code, 405)

    def test_edit_no_request_by_id(self):
        """Tests when no request is found by id when editing"""
        with self.client:
            self.add_request( "", "", "","")
            response = self.put_request("Bulenga", "kawempe", "9","5")
            self.assertEqual(response.status_code, 404)