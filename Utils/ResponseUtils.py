from flask import jsonify

class ResponseUtils:
    @staticmethod
    def success(data=None, message=None):
        response = {'code': 200}

        if data is not None:
            response['data'] = data

        if message is not None:
            response['message'] = message

        return jsonify(response)

    @staticmethod
    def error(message=None):
        response = {'code': '500'}

        if message is not None:
            response['message'] = message

        return jsonify(response)
