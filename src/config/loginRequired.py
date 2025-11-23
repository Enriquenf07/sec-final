from flask import session, redirect, url_for

def login_required(view):
    def wrapper(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("login"))
        return view(*args, **kwargs)
    wrapper.__name__ = view.__name__
    return wrapper