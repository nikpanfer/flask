from flask import Flask, render_template
from blog.users.views import user_blueprint
from blog.articles.views import articles_blueprint


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)

    # @app.route('/')
    # def index():
    #     return render_template('base.html')

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user_blueprint)
    app.register_blueprint(articles_blueprint)