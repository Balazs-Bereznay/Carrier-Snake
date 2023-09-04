from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
import logging


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
logging.basicConfig(filename='demo.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

from app import routes, models