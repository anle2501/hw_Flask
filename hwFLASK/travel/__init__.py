import flask
import os
from flask_sqlalchemy import SQLAlchemy

# instance of the Flask class
myapp = flask.Flask(__name__)
myapp.config.from_mapping(
    SECRET_KEY = 'idk123',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

)
db = SQLAlchemy(myapp)

from travel import routes, models
