from flask import Flask
from flask_migrate import Migrate


def init_app(app: Flask):

    from app.models.model_app import Cards

    Migrate(app, app.db)
