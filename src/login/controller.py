from flask import Blueprint, render_template, redirect, url_for, request
from .service import Service
from flask_login import logout_user
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


@login_bp.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for('login.login'))


