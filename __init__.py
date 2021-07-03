from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
db = SQLAlchemy()
db_name  = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "dfdsfasfaf"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
    db.init_app(app)

    from .auth import auth
    from .views import views
    app.register_blueprint(views , url_prefix = '/')
    app.register_blueprint(auth , url_prefix = '/')
    from .models import User
    create_database(app)
    return  app

def create_database(app):
    if not path.exists('website/' +db_name):
        db.create_all(app =app)
        print('Database created !')