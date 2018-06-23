import uuid
import jwt
import json
from datetime import datetime, timedelta
from flask import current_app


class User():

    def __init__(self, email, password):
        self.id = uuid.uuid4().int
        self.email = email
        self.password = password

    def json(self):
        """
        json representation of the User model
        """

        return json.dumps({
            'id': self.id,
            'email': self.email,
            'password': self.password
        })

    def generate_token(self,user_id):

        try:
            # expiration date of the token
            payload = {
                'exp': datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                # the time the token is generated
                'iat': datetime.utcnow(),
                # the subject of the token (the user whom it identifies)
                'sub': user_id
            }
            # create the byte string token using the payload and the SECRET key
            jwt_string = jwt.encode(
                payload,
                current_app.config.get('SECRET_KEY'),
                algorithm='HS256'
            ).decode('UTF-8')
            return jwt_string

        except Exception as e:
            # return an error in string format if an exception occurs
            return str(e)


    @staticmethod
    def decode_auth_token(self,auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, current_app.config.get('SECRET_KEY'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'


