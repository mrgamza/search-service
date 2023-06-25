from flask import Blueprint, request
from ..service import naver_search_service


blueprint = Blueprint('search', __name__, url_prefix='/search')

@blueprint.route('/', methods=['GET'])
def search():
    query = request.args.get('query')
    return naver_search_service.get_search(query)
