from flask import Flask , redirect ,jsonify , make_response
from api.database import db

def create_app():
    app = Flask(__name__) # create flask instance
    app.config.from_object("config")   # Configure configuration
    
    db.init_app(app=app) # Initialize Flask extensions here

    # Blueprints
    from api.main import main
    app.register_blueprint(blueprint=main,url_prefix='/api')
    from api.participants import participants
    app.register_blueprint(blueprint=participants, url_prefix='/api')

    # Set Error
    from api.errors import errors
    app.register_blueprint(blueprint=errors)


    return app