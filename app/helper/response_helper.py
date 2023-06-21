from app.constant.result_code import ResultCode

class ResponseHelper:
    def response(result_code: ResultCode):
        return {
            'resultCode': result_code.value,
            'resultMessage': result_code.description
        }