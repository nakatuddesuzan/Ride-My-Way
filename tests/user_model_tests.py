import unittest
from app.api.user_model.user import User 
from unittest import TestCase
from app import app
from app.api.user.views import user_list


class TestUserModel(TestCase):

    def test_encode_auth_token(self):
        user = User(
            email='test@test.com',
            password='test'
        )
        user_list.append(user)
        auth_token = user.generate_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))

def test_decode_auth_token(self,):
    user = User(
        email='test@test.com',
        password='test'
    )
    user_list.append(user)
    auth_token = user.generate_token(user.id)
    self.assertTrue(isinstance(auth_token, bytes))
    self.assertTrue(User.decode_auth_token(self,auth_token) == 1)

if __name__ == '__main__':
    unittest.main()
