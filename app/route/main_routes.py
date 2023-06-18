from flask import Blueprint


blue_print = Blueprint('main', __name__, url_prefix='/')

@blue_print.route('/')
def hello():
    return 'Hello, search-service'
