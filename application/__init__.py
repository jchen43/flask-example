from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app():
    app = Flask(__name__)
    
    db.init_app(app)

    with app.app_context():
        from . import routes

        # a bit lazy. ideally have a config file but here for quick in memory db.
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

        # Register routes
        app.register_blueprint(routes.home)

        # create all the sql tables from models
        db.create_all() 

        return app

