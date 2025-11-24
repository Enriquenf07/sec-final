from .repository import Repository
import bcrypt
from flask_login import login_user, current_user
from flask import redirect, url_for
from .model import UserWrapper

class Service:
    @staticmethod
    def validate(form):
        encoded_pass = form["password"].encode()
        print(form)
        user = Repository.find_user_by_login(login=form["login"])
        print(user)
        
        if bcrypt.checkpw(encoded_pass, user[2].encode()):
            userDTO = UserWrapper(user)
            print(userDTO)
            login_user(userDTO)
            return None
        return "Login ou senha inválidos."
    @staticmethod
    def get_roles(id):
        return Repository.get_roles_by_id(id)

    
    
    