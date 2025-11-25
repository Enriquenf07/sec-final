from flask import Flask, render_template, Response, url_for
from login import login_bp
from home import home_bp
from cadastro import cadastro_bp
from userconfig import config_bp
from flask_login import LoginManager
from login import Repository as User_repository
from login import UserWrapper
from config.loguru import configure_loguru
from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv("SECRET_KEY")


def create_app():
    app = Flask(__name__)
    app.register_blueprint(login_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(cadastro_bp)
    app.register_blueprint(config_bp)
    app.secret_key = key
    login_manager = LoginManager()
    login_manager.init_app(app)
    app.config["DEBUG"] = True
    app.config["PROPAGATE_EXCEPTIONS"] = True
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
    configure_loguru()
    return app



app = create_app()


@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    pages = []

    for rule in app.url_map.iter_rules():
        # ignora rotas internas e estáticas
        if "GET" not in rule.methods:
            continue
        if rule.endpoint.startswith("static"):
            continue
        
        # ignora rotas com parâmetros obrigatórios
        if rule.arguments:
            continue

        url = url_for(rule.endpoint, _external=True)
        pages.append(url)

    xml = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]

    for page in pages:
        xml.append(f"  <url><loc>{page}</loc></url>")

    xml.append('</urlset>')

    return Response("\n".join(xml), mimetype='application/xml')

if __name__ == "__main__":
    app.run(debug=True)