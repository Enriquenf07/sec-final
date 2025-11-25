from flask import Blueprint, render_template, redirect, url_for, request
from .service import Service, Repository
from flask_login import logout_user
import secrets
import bcrypt
from config import send_email

login_bp = Blueprint("login", __name__, url_prefix="/login")

@login_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        error = Service.validate(request.form.to_dict())
        if(error != None):
            return redirect(url_for("login.login", message=error))
        return redirect(url_for("home.home"))
    message = request.args.get("message")
    return render_template("pages/login/index.html", message=message)


@login_bp.route("/esqueceu-senha", methods=["GET", "POST"])
def esqueceu_senha():
    if request.method == "POST":
        form = request.form.to_dict()
        user = Repository.find_user_by_login(login=form['login'])
        nova_senha = secrets.token_urlsafe(10)
        hashed = bcrypt.hashpw(nova_senha.encode(), bcrypt.gensalt())
        Repository.nova_senha(hashed.decode(), user[0])
        send_email(
            to=user[4],
            subject="Nova senha",
            contents=f"Olá {user[1]}, sua nova senha temporária: {nova_senha}",
        )
        return redirect(url_for("login.login"))
    return render_template("pages/esqueceu_senha/index.html")
    



@login_bp.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for('login.login'))


