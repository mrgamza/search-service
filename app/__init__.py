from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .route import main_routes, search_routes
    app.register_blueprint(main_routes.blue_print)
    app.register_blueprint(search_routes.blue_print)

    return app
