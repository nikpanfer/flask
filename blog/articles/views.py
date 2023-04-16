from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
from blog.users.views import users

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
def articles_list():
    return render_template('articles/list.html', articles=articles)


@articles_blueprint.route('/<int:pk>')
def get_article(pk: int):
    try:
        article = articles[pk]
    except KeyError:
        raise NotFound(f'article {pk} not found')
    user = users[article['user']]
    return render_template('articles/retrieve.html', article=article, user=user)