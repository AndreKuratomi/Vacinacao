from flask import Blueprint
from app.controllers.app_controller import add_vaccination, get_all

bp_vacc = Blueprint("vaccines", __name__, url_prefix="/vaccinations")

bp_vacc.post("")(add_vaccination)
bp_vacc.get("")(get_all)
