from routes import home

def init_app(app):
    app.register_blueprint(home.calculate)