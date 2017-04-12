import uuid
import hashlib
import requests
import flask
from Code import Users

class Server():
    def __init__(self):
        self.groups = []
        self.server_data = {"users" : {}}


    def create_group(self):
        pass

    def create_user(self, info, password):
        #buscar donde guardo la clave...
        encoded_pass = self.save_password(password)
        new_user = Users.User(info)
        self.server_data["users"][info["id"]] = {new_user}


    def user_login(self):
        pass

    @staticmethod
    def save_password(password):
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ":" + salt

    @staticmethod
    def check_password(real_pass, user_pass):
        password, salt = real_pass.split(":")
        return password == hashlib.sha256(salt.encode() + user_pass.encode()).hexdigest()