from flask import Flask
from app.routes import main_blueprint

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(main_blueprint)
    
    app.config['SECRET_KEY'] = 'your_secret_key'

    return app
