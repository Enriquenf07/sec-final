from login import Repository
import bcrypt
from flask_login import login_user
from login import Repository as User_repository
import secrets
from config import send_email


class Service:
    @staticmethod
    def cadastrar(form): 
        print(form)
        password = form['password'].encode()  
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        if(form.get('name') == None or form.get('name') == ''):
            return "Nome da empresa é obrigatório."
        if(form.get('terms') == None or form.get('terms') != 'on'):
            return "Você deve aceitar os termos de uso."
        if('login' in form and 'email' in form):
            existing_user = User_repository.find_user_by_login(form['login'])
            if existing_user:
                return "Login já existe."
        form['password'] = hashed.decode()
        token = secrets.token_urlsafe(32)
        com_id = User_repository.create_company(form['name'], token)
        user_id = User_repository.create_user(form, com_id)
        User_repository.set_role(user_id, 'admin')
        send_email(
            to=form['email'],
            subject="Cadastro realizado com sucesso",
            contents=f"Olá {form['name-admin']}, seu cadastro foi realizado com sucesso na nossa plataforma. acesse o link para ativar sua conta: http://localhost:5000/cadastro/   ativar?token={token}",
        )
        return None

    @staticmethod
    def ativar(token):
        com_id = User_repository.find_company_by_token(token)
        if(com_id != None):
            User_repository.active_company(com_id)

    
    
    