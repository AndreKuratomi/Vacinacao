from flask import Flask
from app.views.app_routes import bp_vacc


def init_app(app: Flask):
    app.register_blueprint(bp_vacc)
