from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

user_blueprint = Blueprint('user_blueprint', __name__, url_prefix='/users', static_folder='../static')

users = {
    1: 'Nikita',
    2: 'Nasty',
    3: 'Tanya'
}


@user_blueprint.route('/')
def users_list():
    return render_template('users/list.html', users=users)


@user_blueprint.route('/<int:pk>')
def get_user(pk: int):
    try:
        user = users[pk]
    except KeyError:
        raise NotFound(f'user {pk} not found')

    return render_template('users/retrieve.html', user=user)
