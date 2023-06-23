from flask import Blueprint, request

from app.service import naver_search_service

blue_print = Blueprint('search', __name__, url_prefix='/')

@blue_print.route('/search')
def search():
    query = request.args.get('query')
    return naver_search_service.get_search(query)
