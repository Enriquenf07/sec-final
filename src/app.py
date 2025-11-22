from flask import Flask, render_template
from login import login_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(login_bp)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)