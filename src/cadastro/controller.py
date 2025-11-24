from flask import Blueprint, render_template, redirect, url_for, request
from .service import Service
cadastro_bp = Blueprint("cadastro", __name__, url_prefix="/cadastro")

@cadastro_bp.route("/", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        error = Service.cadastrar(request.form.to_dict())
        if(error != None):
            return redirect(url_for("cadastro.cadastro", message=error))
        return redirect(url_for("home.home"))
    message = request.args.get("message")
    return render_template("pages/cadastro/index.html", message=message)

@cadastro_bp.route("/ativar", methods=["GET", "POST"])
def ativar():
    Service.ativar(request.args.get("token"))
    return redirect(url_for("home.home"))
