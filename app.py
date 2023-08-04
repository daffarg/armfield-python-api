from flask import Flask, Blueprint, abort
from flask_cors import CORS
from dotenv import load_dotenv
from http import HTTPStatus

from database.database import Database
from util.response import get_latest_prediction_response, get_data_not_found_response

import os
import pymysql

load_dotenv()

host = os.environ.get('SERVER_HOST', "127.0.0.1")
port = os.environ.get('SERVER_PORT', 5000)

def create_app():
    app = Flask(__name__)
    cors = CORS(app, resources={"api/*": {"origins": "*"}})
    app.register_blueprint(bp, url_prefix='/api')
    return app

db = Database()
bp = Blueprint('api', __name__)

@bp.route("/v1/get-latest-t1", methods=['GET'])
def get_latest_t1():
    try:
        latest_T1_value = db.get_latest_T1_value()
        db.close_connection()
        if not latest_T1_value:
            return get_data_not_found_response()
        response = get_latest_prediction_response(latest_T1_value)
        return response
    except pymysql.MySQLError as sqle:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR, description=str(sqle))
    except Exception as e:
        abort(HTTPStatus.BAD_REQUEST, description=str(e))


@bp.route("/v1/get-latest-t2", methods=['GET'])
def get_latest_t2():
    try:
        latest_T2_value = db.get_latest_T2_value()
        db.close_connection()
        if not latest_T2_value:
            return get_data_not_found_response()
        response = get_latest_prediction_response(latest_T2_value)
        return response
    except pymysql.MySQLError as sqle:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR, description=str(sqle))
    except Exception as e:
        abort(HTTPStatus.BAD_REQUEST, description=str(e))

@bp.route("/v1/get-latest-f1", methods=['GET'])
def get_latest_f1():
    try:
        latest_F1_value = db.get_latest_F1_value()
        if not latest_F1_value:
            return get_data_not_found_response()
        response = get_latest_prediction_response(latest_F1_value)
        return response
    except pymysql.MySQLError as sqle:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR, description=str(sqle))
    except Exception as e:
        abort(HTTPStatus.BAD_REQUEST, description=str(e))

app = create_app()

if __name__ == '__main__':
    app.run(host=host, port=port)