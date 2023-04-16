from flask import Blueprint, redirect, url_for, request, render_template
from flask_login import LoginManager, login_user, login_required, logout_user
from werkzeug.security import check_password_hash

from blog.models import User

auth_blueprint = Blueprint('auth_app', __name__, url_prefix='/auth', static_folder='../static')

login_manager = LoginManager()
login_manager.login_view = "auth_app.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).one_or_none()


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("auth_app.login"))


@auth_blueprint.route("/login/", methods=["GET", "POST"], endpoint="login")
def login():
    if request.method == "GET":
        return render_template("auth/login.html")
    username = request.form.get("username")
    password = request.form.get('password')
    if not username or not password:
        return render_template("auth/login.html", error="username or password not passed")
    user = User.query.filter_by(username=username).one_or_none()
    if not user or not check_password_hash(user.password, password):
        return render_template("auth/login.html", error=f"incorrect username or password")
    login_user(user)
    return redirect(url_for("user_blueprint.users_list"))


@auth_blueprint.route("/logout/", endpoint="logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("user_blueprint.users_list"))
