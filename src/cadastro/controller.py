from flask import Blueprint, render_template, redirect, url_for, request
from .service import Service
from config import Service as config_service
from flask_login import current_user
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


@cadastro_bp.route("/novo_usuario", methods=["GET", "POST"])
def novo_usuario():
    default_ctx = config_service.get_default_ctx()
    
    if not 'admin' in default_ctx['roles']:
        return redirect(url_for("home.home"))
    if request.method == "POST":
        error = Service.cadastrar_funcionario(request.form.to_dict())
        return redirect(url_for("cadastro.novo_usuario"))
    if request.method == "GET":
        users = Service.find_all_by_empresa(current_user.company)
        users = [user for user in users if user["login"] != current_user.login]
        ctx = {"users": users, **default_ctx}
        return render_template("pages/usuarios/index.html", **ctx)