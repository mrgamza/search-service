import os
import urllib.request
import ssl
import json

from flask import Blueprint, request, Response

from app.constant.result_code import ResultCode
from app.helper.response_helper import ResponseHelper


blue_print = Blueprint('search', __name__, url_prefix='/')

@blue_print.route('/search')
def search():
    query = request.args.get('query')
    
    client_id = os.environ.get('NAVER_CLIENT_ID')
    client_secret = os.environ.get('NAVER_CLIENT_SECRET')
    
    encoding_query = urllib.parse.quote(query)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encoding_query
    
    naver_request = urllib.request.Request(url)
    naver_request.add_header("X-Naver-Client-Id", client_id)
    naver_request.add_header("X-Naver-Client-Secret", client_secret)
    
    context = ssl._create_unverified_context()
    naver_response = urllib.request.urlopen(naver_request, context=context)
    
    response = {}
    if naver_response.getcode() is 200:
        response = ResponseHelper.response(ResultCode.SUCCESS)
        response_body = naver_response.read().decode('utf-8')
        response['items'] = json.loads(response_body)['items']
    else:
        response = ResponseHelper.response(ResultCode.NAVER_ERROR)
    
    bytes = json.dumps(response)
    return Response(bytes, mimetype='application/json')
