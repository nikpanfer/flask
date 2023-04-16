from flask.cli import AppGroup
from werkzeug.security import generate_password_hash

from blog.models.database import db

user_cli = AppGroup('user')


@user_cli.command("create")
def create_users():
    """
    Run in your terminal:
    flask create-users
    > done! created users: <User #1 'admin'> <User #2 'james'>
    """
    from blog.models import User
    admin = User(username="admin", password=generate_password_hash('test123'), is_staff=True)
    james = User(username="james", password=generate_password_hash('test123'))
    db.session.add(admin)
    db.session.add(james)
    db.session.commit()
    print("done! created users:", admin, james)