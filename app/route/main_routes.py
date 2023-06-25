from flask import Blueprint


blueprint = Blueprint('main', __name__, url_prefix='/')

@blueprint.route('/', methods=['GET'])
def hello():
    return 'Hello, search-service'
