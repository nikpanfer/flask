from flask.cli import AppGroup

from blog.models.database import db


db_cli = AppGroup('db')


@db_cli.command('init')
def init_db():
    """
    Run in your terminal:
    flask init-db
    """
    db.create_all()
    print("done!")