import os
import sys
# print('\n'.join(sys.path))
sys.path.append('/app/.heroku/python/lib/python3.6/site-packages')
print('\n'.join(sys.path))
from flask import Flask
# from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# app.config.from_object(Config)

app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

login.login_view = 'login'

from app import routes, models
