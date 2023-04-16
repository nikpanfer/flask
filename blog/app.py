from flask import Flask

from blog.auth.views import login_manager, auth_blueprint
from blog.users.views import user_blueprint
from blog.articles.views import articles_blueprint

from blog.models.database import db

from blog.commands import user_cli, db_cli


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = '2ee67e0a93ad9501413c6f5b'

    db.init_app(app)
    login_manager.init_app(app)
    register_blueprints(app)

    register_commands(app)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user_blueprint)
    app.register_blueprint(articles_blueprint)
    app.register_blueprint(auth_blueprint)


def register_commands(app: Flask):
    app.cli.add_command(db_cli)
    app.cli.add_command(user_cli)