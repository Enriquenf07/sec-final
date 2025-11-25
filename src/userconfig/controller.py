from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required,current_user, logout_user
from config import Service as Config_service
from login import Repository as Login_repository
import bcrypt

config_bp = Blueprint("config", __name__, url_prefix="/config")


@config_bp.route("/", methods=["GET", "POST"])
@login_required
def config():
    default_ctx = Config_service.get_default_ctx()
    ctx = {
        "username": current_user.login,
        **default_ctx
    }
    return render_template("pages/config/index.html", **ctx)


@config_bp.route("/desativar", methods=["POST"])
@login_required
def desativar_empresa():
    com_id = current_user.company
    print(com_id)
    Login_repository.desativar_empresa(com_id)
    logout_user()
    return redirect(url_for('login.login'))



@config_bp.route("/nova-senha", methods=["POST"])
@login_required
def nova_senha():
    form = request.form.to_dict()
    nova_senha = form['password']
    hashed = bcrypt.hashpw(nova_senha.encode(), bcrypt.gensalt()).decode('utf-8')
    
    Login_repository.nova_senha(hashed, current_user.id)
    return redirect(url_for('config.config'))
