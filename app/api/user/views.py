import os
import sys
from flask import request
from app import app
from flask import jsonify, make_response,Flask
import re
import json


from ..user_model.user import User
user_list = []

@app.route('/api/user/login')
class Login(User):
    def post (self):
        email= request.json['email']
        password = request.json['password']
        
        user=User(email, password)
        for user in user_list:
            if email == user['email'] and password == user['password']:
                access_token = "{}".format(
                    self.generate_token(user['id']))
                return make_response(jsonify({"token": access_token,
                                              "message": "User logged in successfully"
                                              }), 200)
        return make_response(jsonify({"message": "wrong email or password"}), 401)

@app.route('/api/user/signup', methods=["POST"])
class SignUp (User):
    def post (self):
        first_name = request.json(['first_name'], type=str)
        second_name = request.json['second_name']
        user_name = request.json['user_name']
        email= request.json['email']
        contact=request.json["contact"]
        password = request.json['password']
        verify_password = request.json['verify_password']
       
        if user_name.strip() == "" or len(user_name.strip()) < 2:
            return make_response(jsonify({"message": "invalid, Enter name please"}), 400)

        if re.compile('[!@#$%^&*:;?><.0-9]').match(user_name):
            return make_response(jsonify({"message": "Invalid characters not allowed"}), 400)

        if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", email):
            return make_response(jsonify({"message": "Enter valid email"}), 400)

        if password.strip() == "":
            return make_response(jsonify({"message": "Enter password"}), 400)

        if len(password) < 5:
            return make_response(jsonify({"message": "Password is too short, < 5"}), 400)

        for user in user_list:
            if email == user['email']:
                return make_response(jsonify({"message": "email already in use"}), 400)

        user_list.append({'first_name':first_name, 'second_name':second_name, 'user_name':user_name,
        'email': email,'contact':contact, 'password':password, 'verify_password':verify_password })   

