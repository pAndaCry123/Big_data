from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@host.docker.internal:5434'
db = SQLAlchemy(app)


ma = Marshmallow(app)


from group_b import models,convert_csv,app_schemas,views