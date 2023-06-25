from flask import current_app
from app.constant.result_code import ResultCode
from app.helper.response_helper import ResponseHelper

import os
import urllib.request
import ssl
import json


def get_search(query):
    responseHelper = ResponseHelper()
    
    if not query:
        return responseHelper.response(ResultCode.PARAM_ERROR)
    
    client_id = os.environ.get('NAVER_CLIENT_ID')
    client_secret = os.environ.get('NAVER_CLIENT_SECRET')
    
    encoding_query = urllib.parse.quote(query)
    url = f'https://openapi.naver.com/v1/search/blog?query={encoding_query}'
    
    naver_request = urllib.request.Request(url)
    naver_request.add_header('X-Naver-Client-Id', client_id)
    naver_request.add_header('X-Naver-Client-Secret', client_secret)
    
    context = ssl._create_unverified_context()
    naver_response = urllib.request.urlopen(naver_request, context=context)
    
    if naver_response.getcode() == 200:
        items = json.loads(naver_response.read())['items']
        current_app.logger.info('Success')
        return responseHelper.response(ResultCode.SUCCESS, {'items': items})
    else:
        current_app.logger.info('Fail')
        return responseHelper.response(ResultCode.NAVER_ERROR)
