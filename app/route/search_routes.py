import os
import urllib.request
import ssl
import json

from flask import Blueprint, request, Response


blue_print = Blueprint('search', __name__, url_prefix='/')

@blue_print.route('/search')
def search():
    query = request.args.get('query')
    
    client_id = os.environ.get('NAVER_CLIENT_ID')
    client_secret = os.environ.get('NAVER_CLIENT_SECRET')
    
    encText = urllib.parse.quote(query)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
    
    naver_request = urllib.request.Request(url)
    naver_request.add_header("X-Naver-Client-Id", client_id)
    naver_request.add_header("X-Naver-Client-Secret", client_secret)
    
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(naver_request, context=context)
    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read().decode('utf-8')
        response_to_json = json.loads(response_body)
        response_body = {
            'resultCode': '0000',
            'resultMessage': 'Success',
            'items': response_to_json['items']
        }
        bytes = json.dumps(response_body)
        return Response(bytes, mimetype='application/json')
    else:
        response_body = {
            'resultCode': '1000',
            'resultMessage': 'Naver response code is not 200'
        }
        bytes = json.dumps(response_body)
        return Response(bytes, mimetype='application/json')
