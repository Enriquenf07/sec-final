from flask import Flask, render_template
from login import login_bp
from home import home_bp
from flask_login import LoginManager
from login import Repository as User_repository
from login import UserWrapper

def create_app():
    app = Flask(__name__)
    app.register_blueprint(login_bp)
    app.register_blueprint(home_bp)
    app.secret_key = 'a806WxmuK3vT9rn9gSQ8m9br7NtYc7oX'
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "login.login"
    @login_manager.user_loader
    def load_user(id):
        if(not id):
            return None
        id = int(id)
        row = User_repository.find_user_by_id(id) 
        if not row:
            return None
        return UserWrapper(row)
    return app



app = create_app()

if __name__ == "__main__":
    app.run(debug=True)