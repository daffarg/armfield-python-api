from flask import Flask, Blueprint, jsonify
from flask_cors import CORS
from database.database import Database
from dotenv import load_dotenv
import os

load_dotenv()

host = os.environ.get('SERVER_HOST', "127.0.0.1")
port = os.environ.get('SERVER_PORT', 5000)

def create_app():
    app = Flask(__name__)
    cors = CORS(app, resources={"api/*": {"origins": "*"}})
    app.register_blueprint(bp, url_prefix='/api')
    return app

def get_response_msg(data, status_code):
    message = {
        'status': status_code,
        'data': data if data else 'No records found'
    }
    response_msg = jsonify(message)
    response_msg.status_code = status_code
    return response_msg

db = Database()
bp = Blueprint('api', __name__)

@bp.route("/get-latest-t1")
def get_latest_t1():
    return "<p>T1 Value</p>"

@bp.route("/get-latest-t2")
def get_latest_t2():
    return "<p>T2 Value</p>"

@bp.route("/get-latest-f1")
def get_latest_f1():
    return "<p>F1 Value</p>"

app = create_app()

if __name__ == '__main__':
    app.run(host=host, port=port)