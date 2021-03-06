from flask import Flask
from app.configs import env_configs, database, migrations
from app import views


def create_app(app: Flask):
    app = Flask(__name__)

    env_configs.init_app(app)
    database.init_app(app)
    migrations.init_app(app)
    views.init_app(app)

    return app
