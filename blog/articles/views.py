from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound

from blog.models import User

articles_blueprint = Blueprint('articles_blueprint', __name__, url_prefix='/articles', static_folder='../static')

articles = {
    1: {
        'text': 'qwertytrew',
        'user': 1
    },
    2: {
        'text': 'jhdfavadjv',
        'user': 2
    },
    3: {
        'text': 'fdvkj nakicbiecdwas',
        'user': 2
    }
}


@articles_blueprint.route('/')
@login_required
def articles_list():
    return render_template('articles/list.html', articles=articles)


@articles_blueprint.route('/<int:pk>')
@login_required
def get_article(pk: int):
    try:
        article = articles[pk]
    except KeyError:
        raise NotFound(f'article {pk} not found')
    user = User.query.filter_by(id=article['user']).one()
    return render_template('articles/retrieve.html', article=article, user=user)