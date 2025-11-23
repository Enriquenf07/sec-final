from .repository import Repository
import bcrypt

class Service:
    @staticmethod
    def validate(form):
        encoded_pass = form["password"].encode()
        print(form)
        user = Repository.find_user_by_login(login=form["login"])
        print(user)
        if bcrypt.checkpw(encoded_pass, user[1].encode()):
            print('certo')
            return None
        return "Login ou senha inválidos."