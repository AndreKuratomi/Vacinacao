from flask import current_app, jsonify, request
from app.models.model_app import Cards
from ipdb import set_trace

from exceptions.app_exceptions import AbsentError, NotStringError, WrongLengthError
from sqlalchemy.exc import IntegrityError
from psycopg2.errorcodes import UNIQUE_VIOLATION

valid_keys = ["cpf", "name", "vaccine_name", "health_unit_name"]
check_keys = []


def add_vaccination():
    try:
        previous_data = request.get_json()
        data = {key: previous_data[key] for key in previous_data if key in valid_keys}
        data = {key: values.title() for (key, values) in data.copy().items()}

        new_card = Cards(**data)

        cpf = data['cpf']
        if len(cpf) != 11:
            raise WrongLengthError

        keys = data.keys()
        for elems in keys:
            for sub_elems in valid_keys:
                if elems == sub_elems:
                    check_keys.append(elems)
        if len(check_keys) < 4:
            raise AbsentError

        values = data.values()
        for elems in values:
            if type(elems) != str:
                raise NotStringError

        current_app.db.session.add(new_card)
        current_app.db.session.commit()

        return jsonify(new_card), 201

    except WrongLengthError as wle:
        return wle.message, 400

    except NotStringError as nse:
        return nse.message, 400

    except AbsentError as ae:
        return ae.message, 400

    except IntegrityError as ie:
        if ie.orig.pgcode == UNIQUE_VIOLATION:
            return {"Erro": "CPF já no banco de dados!"}, 409


def get_all():
    vaccines = (Cards.query.all())
    return jsonify(vaccines), 200
