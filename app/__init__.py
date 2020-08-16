
from flask import Flask, url_for
from config import Config
import os

def create_app(object_name=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    return app

app = create_app()

from app import routes, errors