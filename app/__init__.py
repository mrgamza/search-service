import logging

from flask import Flask


def configure_logging():
    logging.basicConfig(
        format = '%(asctime)s:%(levelname)s:%(message)s',
        datefmt = '%m/%d/%Y %I:%M:%S %p',
        level = logging.DEBUG
    )

def create_app():
    app = Flask(__name__)
    configure_logging()
    
    from app.route import main_routes, search_routes
    app.register_blueprint(main_routes.blueprint)
    app.register_blueprint(search_routes.blueprint)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
