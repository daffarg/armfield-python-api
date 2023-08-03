from flask import jsonify

def get_response_msg(message, status_code, data=None):
    message = {
        'status': status_code,
        'message': message, 
    }

    if data:
        message['data'] = data

    response_msg = jsonify(message)
    response_msg.status_code = status_code
    return response_msg

def get_latest_prediction_response(data, status_code):
    return get_response_msg("success", status_code, data[0])

def get_data_not_found_response():
    return get_response_msg("data not found", 404)
