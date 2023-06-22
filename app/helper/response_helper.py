import json

from flask import Response

from app.constant.result_code import ResultCode


class ResponseHelper:
    def __response_body(self, result_code: ResultCode, values = {}):
        response = {
            'resultCode': result_code.value,
            'resultMessage': result_code.description
        }
        
        for key in values:
            response[key] = values[key]
        
        return response
        
    def response(self, result_code: ResultCode, values = {}, mimetype='application/json'):
        response_body = self.__response_body(result_code, values)
        return Response(json.dumps(response_body), mimetype=mimetype)
    