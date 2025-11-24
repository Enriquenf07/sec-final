from flask import Blueprint, render_template, redirect, url_for, request
home_bp = Blueprint("home", __name__, url_prefix="")
from flask_login import login_required,current_user
from config import Service as Config_service


@home_bp.route("/", methods=["GET", "POST"])
@login_required
def home():
    default_ctx = Config_service.get_default_ctx()
    print(default_ctx)
    ctx = {
        "username": current_user.login,
        **default_ctx
    }
    return render_template("pages/home/index.html", **ctx)