import json
from tests.base_tests import BaseTestCase

class Test_auth(BaseTestCase):
    def test_successful_signup(self):
        """
        Test a user is successfully created through the api
        """
        with self.client:
            response = self.SignUP("sue","liam","judg","0774656654","sue@gmail.com","1132018")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertEqual(data.get('message'), "User successfully created")
            resp = self.SignUP("sue","liam","judg","0774656654", "sue@gmail.com", "1132018")
            data1 = json.loads(resp.data.decode())
            self.assertEqual(resp.status_code, 400)
            self.assertEqual(data1.get('message'), "User already exists")

    def test_successful_login(self):
        """
        Test a registered user  is logged in successfully through the api
        """
        with self.client:
            self.SignUP("sue","liam","judg","0774656654","sue@gmail.com","1132018")
            response = self.login_user("sue@gmail.com", "12345")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data.get('message'),"User logged in successfully")

    
    def test_invalid_username_onsignup(self):
        """Test when a user registers with an invalid username"""
        with self.client:
            response = self.SignUP("sue","liam","mag","0774656654","sue@gmail.com","1132018")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertEqual(data.get('message'), "invalid, Enter name please")
            
    def test_username_with_characters_onsignup(self):
        """Test when a user registers with an invalid username with characters"""
        with self.client:
            response = self.SignUP("sue","liam","@!d","0774656654","sue@gmail.com","1132018")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertEqual(data.get('message'), "Invalid characters not allowed")

    def test_when_invalid_email_onsignup(self):
        """Test when invalid email is provided onsignup"""
        with self.client:
            response = self.SignUP("sue","liam","judg","0774656654","liam@gmail.com","1132018")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertEqual(data.get('message'), "Enter valid email")

    def test_when_no_password_onsignup(self):
        """Test when no password onsignup"""
        with self.client:
            response = self.SignUP("sue","liam","judg","0774656654","sue@gmail.com","1132008")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertEqual(data.get('message'), "Enter password")

    def test_when_short_password_onsignup(self):
        """Test when short password is provided onsignup"""
        with self.client:
            response = self.SignUP("sue","liam","judg","0774656654","sue@gmail.com","1132")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertEqual(data.get('message'), "Password is too short, < 5")