from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.models import User

user_blueprint = Blueprint('user_blueprint', __name__, url_prefix='/users', static_folder='../static')


@user_blueprint.route('/')
def users_list():
    users = User.query.all()
    return render_template('users/list.html', users=users)


@user_blueprint.route('/<int:pk>')
def get_user(pk: int):
    user = User.query.filter_by(id=pk).one_or_none()
    if not user:
        raise NotFound(f'user {pk} not found')

    return render_template('users/retrieve.html', user=user)
