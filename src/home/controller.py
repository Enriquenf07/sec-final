from flask import Blueprint, render_template, redirect, url_for, request
home_bp = Blueprint("home", __name__, url_prefix="")



@home_bp.route("/", methods=["GET", "POST"])
def home():
    return render_template("pages/login/index.html", message=message)git 